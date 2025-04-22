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

#### Instalar dependências:
```bash
pip install selenium
```

## 🧪  Como Usar? <a name = "como_usar"></a>
>Antes de executar o arquivo "salvar_cookies.py" tenha em mãos seu email e senha de acesso do linkedin, você tem por padrão 30 segundos para efetuar o login, caso esteja enfrentando dificuldades, altere a linha 8 desse mesmo arquivo para "sleep(60)", agora você terá 60 segundos para efetuar o login. Lembre-se que o programa não é um humano, espere ele fechar sozinho após os segudos designados.
### 1 - Salvar os cookies de login (Execute este script e faça login manual no LinkedIn):
```bash
python salvar_cookies.py
```
>Isso salva um arquivo cookies.pkl, usado nos demais scripts para evitar login repetido.

### 2 - Rodar o script:

#### Usando Terminal 🖥️:
  ```bash
  python Networking_Linkedin.py
  ```
1. O script solicitará a palavra-chave (ex: "desenvolvedor python").
2. Você define quantos convites quer enviar (até 20).
3. Ele faz login, busca perfis e envia os convites automaticamente.

#### Usando Interface Gráfica 💡:
```bash
python bot_linkedin_interface.py
```
1. Insira dentro dos inputs "palavra-chave" e "limite de convites" as informações desejadas.
2. Clique no botão "Executar".
3. Observe o processo na caixa de log.

## 🛡️ Recursos Extras
- > Verificação de usuários (caso vocês já sejam amigos ou o convite já tenha sido enviado ele pula para o próximo, evitando bugs e mantendo a constância na quantia de pedidos designada por você).
- > Cookies de login (em um arquivo que fica no seu próprio computador, serão salvos os dados de sua conta do linkedin, assim você só precisa logar uma única vez, ao invés de ter que fazer isso sempre que precisar usar a automação).
- > Interface interativa (se por ventura você não case muito com o a interface do terminal de seu computador ou editor, desenvolvi uma interface simples no canva e pedi à uma IA que integrasse ela usando o tkinter com o código da automação, assim o programa pode ser usado tendo muito menos contato com o terminal e de uma forma um pouco mais interativa).
- > Automação completa (após configurar a aplicação e logar, você pode deixar ela sem supervisão em segundo plano e sem preocupações, sem a necessidade de um clique se quer).
- > Criação automatica de arquivos necessarios (qualquer arquivo .json ou .pkl que precise existir para que o programa funcione corretamente será criado automaticamente pelo código, evitando assim que você perca seu tempo com isso e o possível mal funcionamento).
- > Lista de perfis visitados (ao fim do processo, dentro da pasta da aplicação existira um arquivo "visitados.json" dentro dele estarão todos os perfis visitados pelo código).
- > Pode ser customizado para rodar diariamente com agendador (ex: cron, task scheduler).

## ⚠️ Atenção
- Automatizar ações no LinkedIn pode violar os termos de uso caso esteja sendo usado de forma indevida. Use por sua conta e risco.
- Limite o número de convites diários para evitar bloqueios.

## 🧠 Ideias Futuras
- Suporte a múltiplas páginas
- Agendamento automático
- Registro de erros em log externo

## ✍️ Autor <a name = "autor"></a>
- [@Ikajira](https://github.com/Ikajira) - Ideia & desenvolvimento do programa.
