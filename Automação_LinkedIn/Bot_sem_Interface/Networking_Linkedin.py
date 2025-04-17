import pickle
import json
import os
from time import sleep
from datetime import datetime
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''Carregar configurações da interface'''
if os.path.exists("config_temp.json"):
    with open("config_temp.json", "r") as f:
        config = json.load(f)
    palavra_chave = config.get("palavra_chave", "desenvolvedor_python")
    lim_convites_diarios = config.get("lim_convites_diarios", 20)
else:
    palavra_chave = "desenvolvedor_python"
    lim_convites_diarios = 20

'''Config'''
palavra_chave = input("Digite a palavra-chave para procurar perfis (ex: 'desenvolvedor_python'): ") or palavra_chave
lim_convites_diarios = int(input("Quantos convites deseja enviar (1-20)? ") or lim_convites_diarios)
max_pag = 1
tempo_espera = 3
arquivo_cookies = "cookies.pkl"

'''Login'''
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/")
sleep(5)

try:
    with open(arquivo_cookies, "rb") as file:
        cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://www.linkedin.com/feed/")
    sleep(3)
    print("✅ Login com cookies realizado.")
except Exception as e:
    print("❌ Erro ao carregar cookies:", e)
    driver.quit()
    exit()

'''Perfis repetidos'''
arquivo_visitados = "visitados.json"
if os.path.exists(arquivo_visitados):
    with open(arquivo_visitados, "r") as f:
        perfis_visitados = set(json.load(f))
else:
    perfis_visitados = set()

'''Busca e Convites'''
visitados = set()
for pagina in range(1, max_pag + 1):
    url = f"https://www.linkedin.com/search/results/people/?keywords={quote(palavra_chave)}&page={pagina}"
    driver.get(url)
    sleep(tempo_espera)

    print(f"🔎 Coletando perfis da página {pagina}")

    links = driver.find_elements(By.XPATH, "//a[contains(@href, '/in/')]")
    for link in links:
        href = link.get_attribute("href")
        if href and href not in visitados and href not in perfis_visitados and "miniProfileURL" not in href:
            visitados.add(href)

print(f"📌 Total de perfis coletados: {len(visitados)}")

convites_env = 0

for i, perfil in enumerate(visitados):
    if convites_env >= lim_convites_diarios:
        print("⛔ Limite diário de convites atingido.")
        break

    print(f"\n👤 Visitando perfil {i + 1}: {perfil}")
    driver.get(perfil)
    sleep(tempo_espera)

    try:
        botoes = driver.find_elements(By.TAG_NAME, "button")
        for botao in botoes:
            texto = botao.text.lower()
            if "conectar" in texto or "connect" in texto:
                botao.click()
                sleep(3)

                # Espera explícita para o pop-up de convite ser visível
                try:
                    print("Aguardando o pop-up de convite...")

                    # Aguardar até que o botão "Enviar sem nota" esteja clicável
                    enviar_cv = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Enviar sem nota']"))
                    )

                    print("Botão 'Enviar sem nota' encontrado. Clicando...")
                    enviar_cv.click()  # Clica no botão "Enviar sem nota"
                    convites_env += 1
                    print(f"✅ Convite {convites_env} enviado.")
                    
                    # Verificar se atingiu o limite de convites e sair do loop
                    if convites_env >= lim_convites_diarios:
                        print("⛔ Limite diário de convites atingido.")
                        break

                except Exception as e:
                    print(f"❌ Erro ao enviar convite sem nota: {e}")
                break
        else:
            print("⚠️ Nenhum botão de conectar disponível.")
    except Exception as e:
        print(f"❌ Erro ao enviar convite: {e}")

    # Verificar se o limite de convites foi atingido antes de continuar
    if convites_env >= lim_convites_diarios:
        break

    sleep(tempo_espera)

'''Perfis Adicionados'''
perfis_visitados.update(visitados)
with open(arquivo_visitados, "w") as f:
    json.dump(list(perfis_visitados), f)

print(f"\n💾 Perfis visitados atualizados no arquivo {arquivo_visitados}")

'''Limitador de Convites'''
arquivo_contador = "contador.json"
data_atual = datetime.now().strftime("%Y-%m-%d")

if os.path.exists(arquivo_contador):
    try:
        with open(arquivo_contador, "r") as f:
            conteudo = f.read().strip()
            if conteudo:
                contador = json.loads(conteudo)
            else:
                contador = {}
    except Exception as e:
        print("⚠️ Erro ao carregar contador:", e)
        contador = {}
    if contador.get("data") != data_atual:
        convites_env = 0
    else:
        convites_env = contador.get("quantidade", 0)
else:
    convites_env = 0

contador = {
    "data": data_atual,
    "quantidade": convites_env
}
with open(arquivo_contador, "w") as f:
    json.dump(contador, f)

print(f"📆 Contador salvo: {convites_env} convite(s) enviados em {data_atual}")

'''Finalizando'''
print("\n🚀 Bot finalizado.")
driver.quit()