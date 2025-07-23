import asyncio
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

async def call_mcp(command: str) -> str:

    process = await asyncio.create_subprocess_exec(
        "uv", "run", "--with", "mcp", "mcp", "run", "server.py",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate(input=command.encode())

    if stderr:
        print("Erro MCP:", stderr.decode())

    return stdout.decode().strip()


async def chat_agent():

    print("Digite sair, exit ou quit para encerrar a conversa.")
    history = [
        {"role": "system", "content": "Você é um assistente de banco de dados."}
    ]

    while True:
        user_message = input("Você: ")
        if user_message.lower() in ["sair", "exit", "quit"]:
            print("Encerrando a conversa.")
            break

        history.append({"role": "user", "content": user_message})

        response = groq_client.chat.completions.create(
            model="llama3-8b-8192",
            messages=history,
            temperature=0,
        )
        assistant_reply = response.choices[0].message.content
        history.append({"role": "assistant", "content": assistant_reply})

        print(f"Assistente: {assistant_reply}")

        if "[MCP]" in assistant_reply:
            cmd = assistant_reply.split("[MCP]")[-1].strip()
            mcp_result = await call_mcp(cmd)
            print(f"[MCP Result]: {mcp_result}")


if __name__ == "__main__":
    asyncio.run(chat_agent())