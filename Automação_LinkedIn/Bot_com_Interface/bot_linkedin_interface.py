import tkinter as tk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json, pickle, os
from time import sleep
from datetime import datetime
import threading
from urllib.parse import quote

# Função principal do bot
def executar_bot(palavra_chave, limite, terminal_output):
    terminal_output.insert(tk.END, f"🔍 Palavra-chave: {palavra_chave} | Limite: {limite}\n")
    terminal_output.see(tk.END)

    max_pag = 1
    tempo_espera = 3
    arquivo_cookies = "cookies.pkl"
    arquivo_visitados = "visitados.json"
    arquivo_contador = "contador.json"
    data_atual = datetime.now().strftime("%Y-%m-%d")

    try:
        driver = webdriver.Chrome()
        driver.get("https://www.linkedin.com/")
        sleep(5)

        # Login com cookies
        if os.path.exists(arquivo_cookies):
            with open(arquivo_cookies, "rb") as file:
                cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.get("https://www.linkedin.com/feed/")
            sleep(3)
            terminal_output.insert(tk.END, "✅ Login com cookies realizado.\n")
        else:
            terminal_output.insert(tk.END, "❌ Arquivo de cookies não encontrado. Faça login e salve os cookies primeiro.\n")
            driver.quit()
            return

        # Carrega perfis visitados
        if os.path.exists(arquivo_visitados):
            with open(arquivo_visitados, "r") as f:
                perfis_visitados = set(json.load(f))
        else:
            perfis_visitados = set()

        visitados = set()
        for pagina in range(1, max_pag + 1):
            url = f"https://www.linkedin.com/search/results/people/?keywords={quote(palavra_chave)}&page={pagina}"
            driver.get(url)
            sleep(tempo_espera)

            terminal_output.insert(tk.END, f"🔎 Coletando perfis da página {pagina}\n")
            links = driver.find_elements(By.XPATH, "//a[contains(@href, '/in/')]")
            for link in links:
                href = link.get_attribute("href")
                if href and href not in visitados and href not in perfis_visitados and "miniProfileURL" not in href:
                    visitados.add(href)

        terminal_output.insert(tk.END, f"📌 Perfis coletados: {len(visitados)}\n")

        convites_env = 0
        for i, perfil in enumerate(visitados):
            if convites_env >= limite:
                terminal_output.insert(tk.END, "⛔ Limite diário de convites atingido.\n")
                break

            driver.get(perfil)
            sleep(tempo_espera)
            terminal_output.insert(tk.END, f"👤 Visitando perfil {i+1}: {perfil}\n")

            try:
                botoes = driver.find_elements(By.TAG_NAME, "button")
                for botao in botoes:
                    texto = botao.text.lower()
                    if "conectar" in texto or "connect" in texto:
                        botao.click()
                        sleep(2)
                        try:
                            enviar_cv = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Enviar sem nota']"))
                            )
                            enviar_cv.click()
                            convites_env += 1
                            terminal_output.insert(tk.END, f"✅ Convite {convites_env} enviado.\n")
                            break
                        except:
                            terminal_output.insert(tk.END, "❌ Erro ao clicar em 'Enviar sem nota'.\n")
                        break
                else:
                    terminal_output.insert(tk.END, "⚠️ Nenhum botão de conectar disponível.\n")
            except Exception as e:
                terminal_output.insert(tk.END, f"❌ Erro no perfil: {e}\n")

            if convites_env >= limite:
                break
            sleep(tempo_espera)

        # Atualiza lista de visitados
        perfis_visitados.update(visitados)
        with open(arquivo_visitados, "w") as f:
            json.dump(list(perfis_visitados), f)

        # Salva contador
        contador = {"data": data_atual, "quantidade": convites_env}
        with open(arquivo_contador, "w") as f:
            json.dump(contador, f)

        terminal_output.insert(tk.END, f"📆 Contador salvo: {convites_env} convite(s) enviados.\n")
        terminal_output.insert(tk.END, "\n🚀 Bot finalizado.\n")
        driver.quit()

    except Exception as e:
        terminal_output.insert(tk.END, f"⚠️ Erro geral: {e}\n")


# Função ao clicar no botão
def rodar_automacao():
    palavra = entrada_palavra.get()
    try:
        limite = int(entrada_limite.get())
        if not (1 <= limite <= 20):
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "O limite deve ser um número entre 1 e 20.")
        return

    terminal_output.insert(tk.END, "🚀 Iniciando automação...\n")
    terminal_output.see(tk.END)

    # Roda o bot em uma thread
    thread = threading.Thread(target=executar_bot, args=(palavra, limite, terminal_output))
    thread.start()


# === Interface ===
janela = tk.Tk()
janela.title("Bot LinkedIn com Interface")
janela.geometry("650x500")
janela.configure(bg="white")

# Título
ttk.Label(janela, text="linkedin_bot.py", font=("Arial", 12, "bold")).pack(pady=10)

# Inputs
frame_inputs = tk.Frame(janela, bg="white", bd=2, relief="ridge")
frame_inputs.pack(pady=10, padx=10)

ttk.Label(frame_inputs, text="Palavra-chave:", font=("Arial", 10)).grid(row=0, column=0, pady=5, padx=5)
entrada_palavra = ttk.Entry(frame_inputs, width=30)
entrada_palavra.grid(row=0, column=1, pady=5, padx=5)
entrada_palavra.insert(0, "desenvolvedor_python")

ttk.Label(frame_inputs, text="Limite de convites (1-20):", font=("Arial", 10)).grid(row=1, column=0, pady=5, padx=5)
entrada_limite = ttk.Entry(frame_inputs, width=10)
entrada_limite.grid(row=1, column=1, pady=5, padx=5, sticky="w")
entrada_limite.insert(0, "10")

ttk.Button(frame_inputs, text="Executar Bot", command=rodar_automacao).grid(row=2, column=0, columnspan=2, pady=10)

# Terminal / Logs
frame_output = tk.Frame(janela, bg="white", bd=2, relief="sunken")
frame_output.pack(expand=True, fill="both", padx=20, pady=10)

terminal_output = tk.Text(frame_output, wrap="word", bg="#F5F5F5", font=("Consolas", 10))
terminal_output.pack(expand=True, fill="both")

# Start
janela.mainloop()