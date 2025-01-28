import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7051719146:AAFAjW2Cgwm5-cdeomVoirLvkOWcL8kCBHA")
    
    API_ID = int(os.environ.get("API_ID", "24720817"))
    
    API_HASH = os.environ.get("API_HASH", "43669876f7dbd754e157c69c89ebf3eb")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    # Add Multiple Picture Using , 
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/dfd1842d8a2dcc536a2b7.jpg https://graph.org/file/b55f0baaa7a6fde7c5682.jpg https://graph.org/file/3298ca8910c82f33418a8.jpg https://graph.org/file/4e4935469a7214c734721.jpg https://graph.org/file/fa5f2b241fe77beff8ba0.jpg https://graph.org/file/bcb9969f78ab4a47a483c.jpg https://graph.org/file/a9af161696d82f17b8888.jpg https://graph.org/file/d23b00650c00ce4d9a467.jpg https://graph.org/file/4dc0b3dfaad61fbcf0a49.jpg https://graph.org/file/7088315e9b0b6a2fa7118.jpg https://graph.org/file/9c9911d06e5f2316febb9.jpg https://graph.org/file/d2ee185180469cfd28071.jpg https://graph.org/file/dea04b2d615406aeb0181.jpg https://graph.org/file/98b63d3bb84984a68cc76.jpg").split()
    
    TG_MAX_FILE_SIZE = 2097152000
    
    FREE_USER_MAX_FILE_SIZE = 2097152000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", "128"))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 0
    
    DEF_WATER_MARK_FILE = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://094:094@cluster0.mixuhkk.mongodb.net/?retryWrites=true&w=majority")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002114592734"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001965228830")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "1235222889"))
    
    # Retrieve the AUTH_USERS environment variable as a space-separated string and convert to a list of integers
    auth_users = [int(user_id) for user_id in os.environ.get('AUTH_USERS', '6571735352').split()]
    
    # Append OWNER_ID to the list of auth_users
    AUTH_USERS = auth_users + [OWNER_ID]
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "upload_ur_url_bot")