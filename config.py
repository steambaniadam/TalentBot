import os

class Config:
    # API credentials
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")

    # Bot credentials
    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    # MongoDB credentials
    DB_URL = os.environ.get("DB_URL")
    DB_NAME = os.environ.get("DB_NAME")

    # Channel IDs
    CHANNEL_1 = os.environ.get("CHANNEL_1")
    CHANNEL_2 = os.environ.get("CHANNEL_2")
    CHANNEL_3 = os.environ.get("CHANNEL_3")
    CHANNEL_LOG = os.environ.get("CHANNEL_LOG")

    # Admin ID
    ID_ADMIN = os.environ.get("ID_ADMIN")

    # Hashtags
    HASHTAG = ["#tag1", "#tag2", "#tag3"]

    # Messages
    PESAN_JOIN = "Selamat datang di grup! 🎉"
    START_MSG = "Halo! Saya adalah bot Telegram, silakan gunakan perintah /start untuk memulai."
    GAGALKIRIM_MSG = "Maaf, pesan tidak dapat dikirim. Silakan coba lagi."

