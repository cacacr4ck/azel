import os
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool
TIME_LIMIT = int(getenv("TIME_LIMIT", "2592000"))
TIME_SLEEP = int(getenv("TIME_SLEEP", "86400"))

load_dotenv(".env")


API_ID = int(getenv("API_ID", "")) #optional
API_HASH = getenv("API_HASH", "")
MONGO_URL = getenv("MONGO_URL")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5569440742").split()))
DEEP_AI = getenv("DEEP_AI", "d7394561-0528-4714-a1ee-edd7020b48e1")
OWNER_ID = int(getenv("OWNER_ID") or 0)
ADMIN1_ID = list(map(int, getenv("ADMIN1_ID", "1086365745").split()))
ADMIN2_ID = list(map(int, getenv("ADMIN2_ID", "5569440742").split()))


ADMIN1_ID.append(1086365745)
ADMIN2_ID.append(5569440742)


BOT_TOKEN = getenv("BOT_TOKEN", "")
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "False"))
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", None)
OPENAI_API = getenv("OPENAI_API", "")
DB_URL = getenv("DATABASE_URL", "postgres://mcclbjwx:CqMrbec47cqL5KbaZOUDlVQWOscjNcKR@peanut.db.elephantsql.com/mcclbjwx")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_WORKERS = int(getenv("BOT_WORKERS", "2"))
USER_WORKERS = int(getenv("BOT_WORKERS", "8"))
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "azazel") #don't change
REPO_URL = getenv("REPO_URL", "https://github.com/ayrizz/Azazel-Project")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SUPPORT = int(getenv("SUPPORT", "-1001812143750"))
CHANNEL = int(getenv("CHANNEL", "-1001896537650"))
SESSION1 = getenv("SESSION1", "")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
