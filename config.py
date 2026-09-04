# config.py

# Telegram Bot Token
bot_token = "8193470148:AAGDmnhrbG23IKg7UIxeM_oU0VCPPQG4QHQ"

# Telethon API credentials
api_id = 2040
api_hash = "b18441a1ff607e10a989891a5462e627"

# Admin chat IDs (list of strings or ints)
admin_chat_ids = [
    "YOUR_ADMIN_ID_HERE",  # <-- вставь свой Telegram ID сюда
]

# CryptoBot token (для оплаты)
CRYPTO_PAY_TOKEN = "YOUR_CRYPTOBOT_TOKEN_HERE"  # если нет — оставь пустым или убери оплату

# Отправители писем (email: password)
senders = {
    "example1@gmail.com": "app_password_here",
    "example2@yahoo.com": "app_password_here",
}

# Получатели жалоб (Telegram support и т.д.)
receivers = [
    "recover@telegram.org",
    "support@telegram.org",
    "abuse@telegram.org",
    "dmca@telegram.org",
]

# SMTP серверы
smtp_servers = {
    "gmail.com": ("smtp.gmail.com", 587),
    "yahoo.com": ("smtp.mail.yahoo.com", 587),
    "mail.ru": ("smtp.mail.ru", 587),
    "yandex.ru": ("smtp.yandex.ru", 587),
    "outlook.com": ("smtp.office365.com", 587),
    "hotmail.com": ("smtp.office365.com", 587),
}
