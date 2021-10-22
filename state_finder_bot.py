import os
import dotenv
import telegram.ext
import requests

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")


def message_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    response = requests.get(f"http://localhost:5000/{update.message.text}").json()
    update.message.reply_text(response['state'])


def main():
    print("initializing updater ...")
    updater = telegram.ext.Updater(TOKEN, use_context=True)
    
    print("initializing dispatcher ...")
    dispatcher = updater.dispatcher
    
    print("initializing message handlers ...")
    dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, message_handler))
    
    print("starting poll ...")
    updater.start_polling()
    
    print("being idle ...")
    updater.idle()


main()
