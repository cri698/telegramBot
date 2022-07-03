
import logging 
import random

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

# Command Handlers
def start(update, context):
    update.message.reply_text('I AM ALIVE!')

# function to respond to help cmd
def help(update, context):
    update.message.reply_text('I am currently not smart enough to help you.')

# function to echo the users message
def echo(update, context):
    update.message.reply_text(update.message.text + '' + ' AND CHRIS IS THE GREATEST.')

# function to log errors and display 
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)



def main():
    updater = Updater("5272042150:AAEx1EXLDzAr0wuhnNuSPNKV-pDASCG7Hj0", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, echo))
    
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()

