import telegram

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import TOKEN

# Define callback functions for handling user input

def start(update, context):

    context.bot.send_message(chat_id=update.message.chat_id, text="Hello! I'm your new bot. How can I help you?")

def echo(update, context):

    context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def unknown(update, context):

    context.bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

# Set up the bot and its handlers

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))

dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))

dispatcher.add_handler(MessageHandler(Filters.command, unknown))

# Start the bot

updater.start_polling()

updater.idle()
