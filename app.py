from telegram.ext import updater
from telegram.ext import CommandHandler, MessageHandler, Filters
import os

TOKEN = os.environ.get('TELEGRAM_ID')


def start(update, context):
    yourname = update.message.chat.first_name

    msg = "hi" + yourname + "! welcome "
    context.bot.send_message(update.message.chat.id, msg)


def mimic(update, context):
    context.bot.send_message(update.message.chat.id, update.message.text)


def details(update, context):
    context.bot.send_message(update.message.chat.id, update.message)


def error(update, context):
    context.bot.send_message(update.message.chat.id, "Oops! Error encountered ")


def main():
    update = Updater(token=TOKEN)

    dp = update.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("details", details))
    dp.add_handler(MessageHandler(Filters.text, mimic))
   
    dp.add_error_handler(error)


#updater.start_webhook(listen="0.0.0.0", port=os.environ.get("PORT", 443),
#                      url_path=TOKEN,
#                      webhook_url="https://telegrambotpython12.app.heroku.com/" + TOKEN)

#updater.idle()

if __name__ == '__main__':
    main()
