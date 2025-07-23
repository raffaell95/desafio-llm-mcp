# Solução desenvolvida para a consulta de dados automotivos.

## A API fornecerá informações de carros cadastrados em banco de dados via protocolo MCP por meio de interação de um agente de IA.

### Tecnologias usadas:

- Python: 3.12
- Sqlalchemy: 2.0.41
- groq: 0.30.0
- faker: 37.4.2
- mcp: 1.12.0
- agents: 1.4.0
- typer: 0.16.0
- sqlite: 3.50.3

### Build
Para que o Agente Groq seja disponibilizado é preciso criar uma chave no site `https://groq.com/` em seguida criar um arquivo .venv dentro da pasta ´src` e adicionar o atributo `GROQ_API_KEY`. Exemplo: GROQ_API_KEY=SUACHAVEGROQ

- Para preparar o ambiente execute os seguintes comandos:
    - 1 - Entrar na pasta do projeto
    - 2 - Criar o ambiente virtual com comando `python -m venv venv`, se você estiver usando o gerenciador `uv`em seguida é so rodar `uv sync` para instalar as dependencias, caso esteja usando `pip` você pode usar `pip install -r requirements.txt`.

- Para rodar os modulos da aplicação é so entrar na pasta `src` e rodar um dos seguintes comandos:

    - Listar os comandos disponiveis no CLI: `python -m cli_test --help`
    - Criar o banco de dados: `python -m cli_test create-database`
    - Popular o banco de dados: `python -m cli_test create-cars`
    - listar os dados: `python -m cli_test get-cars

    - Testar a conexão com server MCP: `python -m clent_test`
    - Interagir com chat/client: `python -m chat`
    - Executar somente o server MCP: `mcp dev server.py`, ele vai abrir em uma interface web, é necessario ter o `nodejs`instalado.
