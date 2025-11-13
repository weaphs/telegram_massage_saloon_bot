# 💆‍♀️ Massage Studio Telegram Bot

A modern Telegram bot for managing bookings at a massage studio.  
Built with **Aiogram 3**, **PostgreSQL**, **SQLAlchemy**, and **APScheduler**.  
The bot allows clients to make appointments, automatically sends reminders, and stores all data in a database.

---

## 🚀 Features

✅ User registration and booking process  
✅ Automatic appointment reminders (1 hour before the visit)  
✅ Database integration (PostgreSQL + SQLAlchemy)  
✅ Asynchronous architecture using Aiogram 3  
✅ Scheduler for background tasks (APScheduler)  
✅ Environment configuration via `.env`  
✅ Clean modular project structure  

---

## 🧩 Project Structure
```
telegram_massage_saloon_bot/
    ├── bot/
    │   ├── handlers/ # Message & callback handlers (booking, start, etc.)
    │   ├── keyboards/ # Inline and reply keyboards
    │   ├── fsm/ # FSM (user states for multi-step dialogs)
    │   ├── scheduler/ # APScheduler jobs for reminders
    │   ├── init.py
    │   └── bot.py
    │├── config/
    │   ├── settings.py # Environment variables and configuration
    │   └── init.py
    │├── db/
    │   ├── crud.py # Database CRUD operations
    │   ├── models.py # SQLAlchemy ORM models
    │   ├── database.py # Async database session setup
    │   └── init.py
    │├── utils/
    │   ├── time_slots.py # Helper for generating available time slots
    │   └── init.py
    │├── main.py # Entry point (starts the bot)
    ├── requirements.txt # Project dependencies
    ├── .env # Environment variables (ignored in git)
    ├── .gitignore # Git ignore rules
    └── README.md # Project documentation
```
---
## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/massage-studio-bot.git
cd massage-studio-bot
```
### 2️⃣ Create and activate a virtual environment
```
python -m venv .venv
source .venv/bin/activate   # On macOS/Linux
# or
.venv\Scripts\activate      # On Windows
```
### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```
### 🗄️ Database Setup (PostgreSQL)

Make sure PostgreSQL is installed and running.

Create a database for the bot:
```
createdb massage_bot_db
```
Set your connection string in the .env file (see below).
### 🔑 Environment Configuration

Create a .env file in the root directory and fill it like this:
```
BOT_TOKEN=
DB_HOST=
DB_PORT=
DB_USER=
DB_PASS=
DB_NAME=
```
⚠️ The .env file is ignored by git (see .gitignore),
so your secrets will remain private.

### ▶️ Run the Bot

```
python main.py
```

## Created by Hryhorii





