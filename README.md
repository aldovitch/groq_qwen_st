# Chat Qwen com Streamlit e Groq

Aplicação de chat desenvolvida com **Streamlit**, **LangChain** e **Groq**, utilizando o modelo **Qwen**.

O projeto demonstra uma implementação simples de uma interface conversacional com histórico de mensagens mantido durante a sessão.

## Tecnologias

- Python 3.10+
- Streamlit
- LangChain
- langchain-groq
- python-dotenv
- Groq
- Qwen

## Modelo utilizado

O projeto utiliza o modelo:

`qwen/qwen3.6-27b`

## Instalação

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

Crie e ative um ambiente virtual:

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_da_groq
```

A chave da API deve ser obtida na plataforma Groq.

**Nunca publique sua chave da API no GitHub.**

Recomenda-se adicionar ao `.gitignore`:

```text
.env
.venv/
__pycache__/
```

## Execução

Execute a aplicação com:

```bash
streamlit run app.py
```

Depois, acesse a URL apresentada pelo Streamlit, normalmente:

```text
http://localhost:8501
```

## Funcionalidades

- Interface de chat utilizando Streamlit
- Histórico de mensagens durante a sessão
- Contexto da conversa enviado ao modelo
- Botão para limpar o histórico
- Integração com o modelo Qwen através da Groq

## Estrutura do projeto

```text
.
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> O arquivo `.env` é utilizado apenas localmente e não deve ser enviado para o repositório.

## Dependências

As principais dependências estão definidas em `requirements.txt`:

```text
streamlit
langchain-groq
python-dotenv
```

## Licença

Este projeto é disponibilizado para fins de estudo e experimentação.
