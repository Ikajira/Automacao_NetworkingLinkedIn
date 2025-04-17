# Bot de Networking para LinkedIn

Este projeto automatiza o envio de convites no LinkedIn com base em uma palavra-chave definida pelo usuário. Ele utiliza **Python + Selenium** para controlar o navegador e possui uma **interface gráfica com Tkinter** para facilitar o uso.

## 📁 Estrutura dos Arquivos

| Arquivo                    | Descrição                                                                 |
|---------------------------|---------------------------------------------------------------------------|
| `Networking_Linkedin.py`  | Script principal de automação via terminal                                |
| `salvar_cookies.py`       | Script auxiliar para salvar os cookies após login manual                  |
| `bot_linkedin_interface.py` | Interface gráfica Tkinter para uso amigável da automação                 |
| `cookies.pkl`             | Arquivo gerado com os cookies de login do LinkedIn                        |
| `visitados.json`          | Armazena perfis já visitados para evitar duplicação                       |
| `contador.json`           | Registra quantos convites foram enviados por dia                          |
| `config_temp.json`        | (opcional) Arquivo gerado pela interface com configurações temporárias    |

## ⚙️ Pré-requisitos

- Python 3.7+
- Google Chrome instalado
- WebDriver do Chrome compatível (e no PATH)
- Instalar dependências:
  ```bash
  pip install selenium

## 🧪  Como Usar? <a name = "como_usar"></a>
### 1° Salvar os cookies de login (Execute este script e faça login manual no LinkedIn):
```bash
python salvar_cookies.py
```
>Isso salva um arquivo cookies.pkl, usado nos demais scripts para evitar login repetido.

### 2° Rodar o script:
- Usar via Terminal
  ```bash
  python Networking_Linkedin.py
  ```
1. O script solicitará a palavra-chave (ex: "desenvolvedor python").
2. Você define quantos convites quer enviar (até 20).
3. Ele faz login, busca perfis e envia os convites automaticamente.

- Usar via Interface Gráfica
```bash
python bot_linkedin_interface.py
```
1. Interface amigável com inputs para palavra-chave e limite de convites
2. Exibe logs em tempo real
3. Ideal para quem prefere não usar o terminal

## 🛡️ Recursos Extras
- 1° Evita perfis repetidos usando visitados.json
- 2° Limite diário de convites salvo em contador.json
- 3° Login persistente com cookies
- 4° Pode ser customizado para rodar diariamente com agendador (ex: cron, task scheduler)

## ⚠️ Atenção
- Automatizar ações no LinkedIn pode violar os termos de uso. Use por sua conta e risco.
- Limite o número de convites diários para evitar bloqueios.

## 🧠 Ideias Futuras
- Suporte a múltiplas páginas
- Enviar mensagem personalizada com convite
- Agendamento automático
