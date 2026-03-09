# Userbot Things 🤖



A lightweight, modular, and efficient Telegram Userbot built with Python. This project is designed to automate personal account tasks, provide utility commands, and streamline your Telegram experience directly from your chat interface.

## 🚀 Features

* **Utility Tools**: Built-in commands for text formatting, media management, and advanced chat navigation.
* **Automation**: Task-handling logic designed to run in the background.
* **Modular Design**: Structured for easy extension. You can add custom handlers or plugins without cluttering the main codebase.
* **Lightweight**: Optimized for minimal resource usage and fast execution.

## 🏗 How it Works

Unlike standard bots, this project uses the **MTProto protocol** to interact with Telegram servers. It acts on your behalf, meaning it performs actions as if you were typing from your phone or desktop app.

```
[Telegram Servers] <---> [Userbot Script]
                              ^
                              |
                     [Your Telegram Account]
```
# 🛠 Setup Instructions
### 1. Prerequisites
Python 3.10+ installed on your system.

An API ID and API Hash obtained from my.telegram.org.

### 2. Installation
Clone the repository:
```
git clone [https://github.com/gutigomd/userbot_things.git](https://github.com/gutigomd/userbot_things.git)
cd userbot_things
```
Install dependencies:
```
pip install -r requirements.txt
```
Setup environment variables:
Create a .env file in the root directory and add your credentials. Never commit this file to GitHub.
```
API_ID=your_api_id
API_HASH=your_api_hash
SESSION_NAME=my_userbot
```
Run the bot:
```
python main.py
```
# 🛡 Safety and Disclaimer
### ⚠️ Important Usage Warning:
This project is a Userbot. It performs actions directly on your personal Telegram account.

Compliance: Telegram's Terms of Service prohibit spamming or automated mass-messaging. Use this tool only for personal automation and productivity.

Account Ban Risk: Excessive API calls or suspicious behavior can lead to account restrictions or bans. You are responsible for your account activity.

Data Security: Never share your SESSION_NAME.session file or your API credentials with anyone.

Disclaimer: I am not responsible for any account limitations, bans, or technical issues that may arise from using this script. Use this tool at your own risk.
