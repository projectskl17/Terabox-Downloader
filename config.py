from os import environ

# BOT CONFIG
API_ID = environ.get("API_ID")  # api id
API_HASH = environ.get("API_HASH")  # api hash
BOT_TOKEN = environ.get("BOT_TOKEN")  # bot token

# REDIS
REDIS_HOST = environ.get("REDIS_HOST")  # redis host uri
REDIS_PORT = environ.get("REDIS_PORT")  # redis port
REDIS_PASSWORD = environ.get("REDIS_PASSWORD")  # redis password

# Admin and Chat Configuration
ADMINS = list(map(int, environ.get("ADMINS", "6791744215").split(',')))  # admin ids
OWNER_ID = int(environ.get("OWNER_ID", 6791744215))  # Replace with your Telegram user ID
PRIVATE_CHAT_ID = int(environ.get("PRIVATE_CHAT_ID", -100))  # Chat where you want to store videos
USER_CHANNEL = int(environ.get("USER_CHANNEL", -100))
DUMP_CHANNEL = int(environ.get("DUMP_CHANNEL", -100))

# Config
COOKIE = environ.get("COOKIE")  # cookie
