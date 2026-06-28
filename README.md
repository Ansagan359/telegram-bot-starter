# Telegram Bot Starter

A clean, **production-ready boilerplate** for building Telegram bots fast, built with [aiogram 3](https://docs.aiogram.dev/). Typed configuration, modular routers, middlewares and Docker support — fork it and start shipping in minutes.

<p>
  <img src="https://img.shields.io/badge/Python-3.11+-141417?style=flat-square&logo=python&logoColor=6e56f7" />
  <img src="https://img.shields.io/badge/aiogram-3.x-141417?style=flat-square&logo=telegram&logoColor=6e56f7" />
  <img src="https://img.shields.io/badge/license-MIT-141417?style=flat-square" />
  <img src="https://img.shields.io/badge/code%20style-ruff-141417?style=flat-square" />
</p>

> **Demo**
>
> <!-- Replace with a real screenshot / GIF of your bot in action -->
> ![Bot demo](https://placehold.co/800x400/0a0a0b/6e56f7?text=Telegram+Bot+Starter)

---

## ✨ Features

- ⚡ **aiogram 3** with modern async routers
- 🧩 **Modular structure** — handlers, keyboards, middlewares cleanly separated
- 🔐 **Typed config** via `pydantic-settings` (`.env` driven)
- 🎛 **Inline menu** example with callback navigation
- 🪵 **Logging middleware** out of the box
- 🐳 **Docker & docker-compose** ready
- 🧹 **Ruff**-configured, type-hinted, zero magic

## 🗂 Project structure

```
telegram-bot-starter/
├── bot/
│   ├── __main__.py        # entry point (python -m bot)
│   ├── config.py          # typed settings from .env
│   ├── handlers/          # start, common (help/about), echo
│   ├── keyboards/         # inline keyboards
│   ├── middlewares/       # logging middleware
│   └── utils/             # logging setup
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── requirements.txt
└── README.md
```

## 🚀 Quick start

```bash
# 1. Clone
git clone https://github.com/Ansagan359/telegram-bot-starter.git
cd telegram-bot-starter

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure
cp .env.example .env             # then add your BOT_TOKEN

# 5. Run
python -m bot
```

Get a token from [@BotFather](https://t.me/BotFather), paste it into `.env`, and send `/start` to your bot.

## ⚙️ Configuration

| Variable | Required | Default | Description |
| --- | :---: | --- | --- |
| `BOT_TOKEN` | ✅ | — | Token from @BotFather |
| `ADMIN_IDS` | ❌ | empty | Comma-separated admin user IDs |
| `LOG_LEVEL` | ❌ | `INFO` | `DEBUG` / `INFO` / `WARNING` / `ERROR` |

## 🐳 Docker

```bash
docker compose up --build -d
```

The bot reads its configuration from `.env` and restarts automatically unless stopped.

## 🧱 Adding a new command

1. Create a handler in `bot/handlers/`, e.g. `ping.py`:

   ```python
   from aiogram import Router
   from aiogram.filters import Command
   from aiogram.types import Message

   router = Router(name="ping")

   @router.message(Command("ping"))
   async def ping(message: Message) -> None:
       await message.answer("pong 🏓")
   ```

2. Register it in `bot/handlers/__init__.py` (keep `echo` last).

## 🤝 Contributing

Issues and pull requests are welcome. Please keep the code typed and run `ruff check .` before submitting.

## 📄 License

[MIT](LICENSE) © Ansagan
