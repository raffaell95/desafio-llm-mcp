import asyncio
import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq
from functools import partial

load_dotenv()

# Inicializa cliente Groq
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# Função para rodar MCP (subprocesso)
async def call_mcp(command: str) -> str:
    process = await asyncio.create_subprocess_exec(
        "uv", "run", "--with", "mcp", "mcp", "run", "server.py",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate(input=command.encode())

    if stderr:
        return f"Erro MCP: {stderr.decode()}"

    return stdout.decode().strip()


# Função para obter resposta do Groq (executa em thread pool)
async def get_groq_response(history):
    loop = asyncio.get_running_loop()
    response = await loop.run_in_executor(
        None,
        partial(
            groq_client.chat.completions.create,
            model="llama3-8b-8192",
            messages=history,
            temperature=0,
        )
    )
    return response.choices[0].message.content


# Interface Streamlit
st.set_page_config(page_title="Assistente MCP", page_icon="🤖", layout="centered")
st.title("🤖 Assistente de Banco de Dados (Groq + MCP)")

# Inicializa histórico na sessão
if "history" not in st.session_state:
    st.session_state.history = [
        {"role": "system", "content": "Você é um assistente de banco de dados."}
    ]
    st.session_state.messages = []

# Exibe histórico
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# Input do usuário
if prompt := st.chat_input("Digite sua pergunta ou comando..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.history.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                assistant_reply = asyncio.run(get_groq_response(st.session_state.history))
            except Exception as e:
                assistant_reply = f"Erro ao chamar Groq: {e}"

            st.markdown(assistant_reply)
            st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
            st.session_state.history.append({"role": "assistant", "content": assistant_reply})

            # Se a resposta contém um comando MCP
            if "[MCP]" in assistant_reply:
                cmd = assistant_reply.split("[MCP]")[-1].strip()
                with st.spinner(f"Executando MCP: {cmd}"):
                    mcp_result = asyncio.run(call_mcp(cmd))
                    st.markdown(f"**[MCP Result]:** {mcp_result}")
                    st.session_state.messages.append({"role": "assistant", "content": f"[MCP Result]: {mcp_result}"})
