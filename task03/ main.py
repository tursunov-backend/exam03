from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from image_bot import ImageBot
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    BOT_TOKEN = os.getenv("BOT_TOKEN")


settings = Settings()


def main():
    bot = ImageBot(settings.BOT_TOKEN)

    updater = Updater(settings.BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", bot.handlers.start_command))
    dp.add_handler(CommandHandler("dog", bot.handlers.dog_command))
    dp.add_handler(CommandHandler("cat", bot.handlers.cat_command))
    dp.add_handler(CommandHandler("fox", bot.handlers.fox_command))
    dp.add_handler(CallbackQueryHandler(bot.handlers.button_handler))


    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
