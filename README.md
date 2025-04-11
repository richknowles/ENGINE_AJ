![Engine AJ](https://img.shields.io/badge/Status-In%20Progress-blue?style=for-the-badge&logo=whatsapp)

![ENGINE_AJ-GH-Banner_v1@0 5x](https://github.com/user-attachments/assets/51236719-9660-4e7c-a994-99bd541a4deb)

# ENGINE AJ

Engine AJ is a stealthy WhatsApp Web automation tool designed to send messages in a human-like way. It mimics natural behavior to avoid detection and bans while delivering batch messages efficiently.

---

## Features
- Uses `undetected-chromedriver` to reduce risk of WhatsApp bans
- Simulates human interaction with random scrolls, typing delays, and mouse movement
- Easy CSV-based batch messaging
- Requires no WhatsApp Business account

---

## Setup Instructions

### 1. Install Dependencies (macOS)
```bash
brew install python3
pip3 install selenium undetected-chromedriver python-dotenv pandas
brew install --cask google-chrome
```

### 2. Run the App
```bash
python3 launcher.py
```

---

## File Structure

- `main.py` – Handles flow
- `launcher.py` – Starts the engine
- `recipients.csv` – Phone numbers and messages
- `app/aj_driver.py` – Chrome driver init
- `app/aj_sender.py` – Messaging logic
- `app/aj_utils.py` – Human-like behavior functions

---

## LICENSE
©2025 Rich Knowles – Released under GPLv3
