# Telegram Llama 3 Bot

A Telegram bot powered by a local Llama 3 LLM via Ollama.

## Features

- `/start` — greeting
- `/help` — list of available commands
- `/prompt [text]` — send a request to the assistant
- `/forgot` — clear the current context
- `/load` — restore the context from the database

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com/) with the `llama3` model
- A Telegram bot token from [@BotFather](https://t.me/BotFather)

## Installation

```bash
git clone https://github.com/USERNAME/REPO.git
cd REPO
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and set your token:

```
TOKEN=1234567890:AAH...
```

Pull the Llama 3 model:

```bash
ollama pull llama3
```

## Running

```bash
python main.py
```

## License

MIT