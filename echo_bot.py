import os
import dotenv
import telegram.ext

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")


def message_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    update.message.reply_text(update.message.text)


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
