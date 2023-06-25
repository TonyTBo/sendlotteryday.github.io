
__author__ = 'Khiem Doan'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'

from functools import lru_cache

from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings
# from telegram import Bot
from telegram.bot import Bot


class TelegramSettings(BaseSettings):
    bot_token: str = Field(alias='TELEGRAM_BOT_TOKEN')
    chat_id: str = Field(alias='TELEGRAM_CHAT_ID')


@lru_cache
def get_telegram_settings() -> TelegramSettings:
    try:
        return TelegramSettings()
    except ValidationError:
        pass

    return TelegramSettings(_env_file='.env')


async def send_message(message: str) -> bool:
    settings = get_telegram_settings()
    print(settings)
    bot = Bot(settings.bot_token)
    try:
        await bot.send_message(settings.chat_id, message)
    except:
        return False
    return True
