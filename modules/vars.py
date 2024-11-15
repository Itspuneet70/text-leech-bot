import os

API_ID    = os.environ.get("API_ID", "29937683")
API_HASH  = os.environ.get("API_HASH", "5f6d4ca9ffadd037db94446dc7c0d6fa")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
