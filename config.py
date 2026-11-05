import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

# ==========================================
# LOAD ENVIRONMENT
# ==========================================

load_dotenv()


# ==========================================
# TELEGRAM API CONFIGURATION
# ==========================================

API_ID = int(getenv("API_ID", "38897826"))
API_HASH = getenv("API_HASH", "e44640b6b8de2cf53b002cf02489b2e4")

BOT_TOKEN = getenv("BOT_TOKEN", "9101883659:AAGd0tWmuW6dMFmp7nAA04-FLYRxQM9R7wE")


# ==========================================
# MONGODB DATABASE CONFIGURATION
# ==========================================

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://temetiger360_db_user:ZVsiJTPn8ylGHLjW@facebooksell.a7bx1ev.mongodb.net/?appName=Facebooksell")


# ==========================================
# OWNER CONFIGURATION
# ==========================================

OWNER_ID = int(getenv("OWNER_ID", "2014144404"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-5481620689"))


# ==========================================
# MUSIC CONFIGURATION
# ==========================================

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "1700"))

PLAYLIST_FETCH_LIMIT = int(
    getenv("PLAYLIST_FETCH_LIMIT", "25")
)


# ==========================================
# TELEGRAM FILE SIZE LIMIT
# ==========================================

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "2145386496")
)


# ==========================================
# YOUTUBE API CONFIGURATION
# ==========================================

API_URL = getenv(
    "API_URL",
    "https://apisparrow.site"
)

API_KEY = getenv("API_KEY", "sparrowyjxrNvwMbwzO0kJhEzMRLUGv")


# ==========================================
# ASSISTANT SESSION CONFIGURATION
# ==========================================

STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", "")
STRING3 = getenv("STRING_SESSION3", "")
STRING4 = getenv("STRING_SESSION4", "")
STRING5 = getenv("STRING_SESSION5", "")


# ==========================================
# SPOTIFY CONFIGURATION
# ==========================================

SPOTIFY_CLIENT_ID = getenv(
    "SPOTIFY_CLIENT_ID",
    ""
)

SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET",
    ""
)


# ==========================================
# SUPPORT CONFIGURATION
# ==========================================

SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL",
    "https://t.me/babylav"
)

SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP",
    "https://t.me/babylav"
)


# ==========================================
# PRIVACY POLICY
# ==========================================

PRIVACY_LINK = getenv(
    "PRIVACY_LINK",
    "https://telegra.ph/Privacy-Policy-for-MusicSp-08-14"
)


# ==========================================
# ASSISTANT AUTO LEAVING
# ==========================================

AUTO_LEAVING_ASSISTANT = (
    getenv("AUTO_LEAVING_ASSISTANT", "False").lower()
    in ("true", "1", "yes", "on")
)


# ==========================================
# GITHUB UPSTREAM CONFIGURATION
# ==========================================

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/DevloperSP/MusicSp"
)

UPSTREAM_BRANCH = getenv(
    "UPSTREAM_BRANCH",
    "main"
)

GIT_TOKEN = getenv("GIT_TOKEN", "")


# ==========================================
# HEROKU CONFIGURATION
# ==========================================

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")

HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")


# ==========================================
# INTERNAL BOT VARIABLES
# ==========================================

BANNED_USERS = filters.user()

adminlist = {}

lyrical = {}

votemode = {}

autoclean = []

confirmer = {}


# ==========================================
# IMAGE CONFIGURATION
# ==========================================

START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/sunset_mountain.jpg"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/starry_night.jpg"
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/starry_night.jpg"
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/sunset_mountain.jpg"
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/morning_sunrise.jpg"
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/morning_sunrise.jpg"
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/morning_sunrise.jpg"
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/music_forest.jpg"
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/morning_sunrise.jpg"
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/music_forest.jpg"
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/music_forest.jpg"
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "https://raw.githubusercontent.com/DevloperSP/MusicSp/main/.assets/music_forest.jpg"
)


# ==========================================
# TIME CONVERSION
# ==========================================

def time_to_seconds(time):

    stringt = str(time)

    return sum(
        int(x) * 60**i
        for i, x in enumerate(
            reversed(stringt.split(":"))
        )
    )


DURATION_LIMIT = int(
    time_to_seconds(f"{DURATION_LIMIT_MIN}:00")
)


# ==========================================
# URL VALIDATION
# ==========================================

if SUPPORT_CHANNEL:

    if not re.match(r"^https?://", SUPPORT_CHANNEL):

        raise SystemExit(
            "[ERROR] Invalid SUPPORT_CHANNEL URL"
        )


if SUPPORT_GROUP:

    if not re.match(r"^https?://", SUPPORT_GROUP):

        raise SystemExit(
            "[ERROR] Invalid SUPPORT_GROUP URL"
        )


# ==========================================
# REQUIRED CONFIGURATION CHECK
# ==========================================

required_config = {
    "API_ID": API_ID,
    "API_HASH": API_HASH,
    "BOT_TOKEN": BOT_TOKEN,
    "MONGO_DB_URI": MONGO_DB_URI,
    "OWNER_ID": OWNER_ID,
    "LOG_GROUP_ID": LOG_GROUP_ID,
}

missing_config = [
    key for key, value in required_config.items()
    if not value
]

if missing_config:

    raise SystemExit(
        "[CONFIG ERROR] Missing Railway Variables: "
        + ", ".join(missing_config)
    )


print("================================")
print(" MusicSp Configuration Loaded ")
print(" Telegram Configuration: OK ")
print(" MongoDB Configuration: OK ")
print(" Owner Configuration: OK ")
print(" Music Configuration: OK ")
print("================================")
