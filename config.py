from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    BOT_TOKEN : str = str(os.getenv("BOT_TOKEN"))
    GUILD_ID = int(os.getenv("GUILD_ID"))
    LOG_CHANNEL_ID  : int = int(os.getenv("LOG_CHANNEL_ID"))
    MUTE_ROLE_NAME = os.getenv("MUTE_ROLE_NAME", "Muted")
    BAD_WORDS = os.getenv("BAD_WORDS", "").split(",")
    COMMAND_PREFIX = os.getenv("COMMAND_PREFIX", "!")
    

settings = Settings()

if __name__ == "__main__":
    print(type(settings.BOT_TOKEN))