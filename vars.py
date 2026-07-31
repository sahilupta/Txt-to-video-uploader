
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "28221704"))
API_HASH = environ.get("API_HASH", "a0163f47bc5262a3106b7858720a09fb")
BOT_TOKEN = environ.get("BOT_TOKEN", "8842602749:AAECqZU_dC4mdqrymIb7cmA8HZqylD144tM")

OWNER = int(environ.get("OWNER", "8321801403"))
CREDIT = environ.get("CREDIT", "𝙎𝘼HIL 𝘽𝙊𝙏𝙎")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8321801403').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8321801403').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
