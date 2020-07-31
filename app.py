import os
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

from tools.api_tools.api_tools import MessHandler as MH
from app_config import app_token, app_url

TOKEN = app_token
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler("start", MH.start))
updater.dispatcher.add_handler(CommandHandler("crypt", MH.crypt))
updater.dispatcher.add_handler(CommandHandler("encrypt", MH.encrypt))
updater.dispatcher.add_handler(CommandHandler("getmode", MH.getmode))

updater.dispatcher.add_handler(MessageHandler(Filters.text, MH.text_handler))

updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.set_webhook(app_url + TOKEN)

updater.idle()
