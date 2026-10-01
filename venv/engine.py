import ollama
from database.db import save_message, get_history

class Llama3Engine:
    def __init__(self, model_name: str = "llama3"):
        self.host = "http://localhost:11434"
        self.client = ollama.AsyncClient(host=self.host)
        self.model_name = model_name

        self.contexts: dict[int, list] = {}

    async def ask(self, user_id, prompt: str, role: str = "user") -> str:
        history = self.contexts.setdefault(user_id, [])
        history.append({"role": role, "content": prompt})

        save_message(user_id, "user", prompt)

        response = await self.client.chat(
            model=self.model_name,
            messages=history,
        )

        answer = response["message"]["content"]
        history.append({"role": "assistant", "content": answer})
        save_message(user_id, "assistant", answer)

        return answer

    async def delete_context(self, user_id: int) -> None:
        self.contexts.pop(user_id, None)

    async def load_context(self, user_id: int):
        rows = get_history(user_id)
        self.contexts[user_id] = [{"role": r, "content": c} for r, c in rows]
        return self.contexts[user_id]