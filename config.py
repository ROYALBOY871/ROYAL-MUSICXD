from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "10534530"))
API_HASH = getenv("API_HASH", "8760d7849212237231adda6255eec300")
BOT_TOKEN = getenv("BOT_TOKEN","1917637742:AAF61TOx72pQEap0aHp56t9yQL5VUl-C7R0")
BOT_NAME = getenv("BOT_NAME","ROYAL-MUSICXD❤️")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "session")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1995146480").split()))
