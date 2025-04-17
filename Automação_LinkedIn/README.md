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