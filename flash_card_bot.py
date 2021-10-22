import os
import dotenv
import telegram.ext

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")


def start_command_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    keyboard = [
        [
            telegram.InlineKeyboardButton("Answer", callback_data='answer'),
        ],
    ]
    
    update.message.reply_text("Book", reply_markup=telegram.InlineKeyboardMarkup(keyboard))


def question_handler(query) -> None:
    keyboard = [
        [
            telegram.InlineKeyboardButton("Answer", callback_data='answer'),
        ],
    ]
    
    query.edit_message_text("Book", reply_markup=telegram.InlineKeyboardMarkup(keyboard))


def answer_handler(query) -> None:
    keyboard = [
        [
            telegram.InlineKeyboardButton("Question", callback_data='question'),
        ],
    ]
    
    query.edit_message_text("کتاب", reply_markup=telegram.InlineKeyboardMarkup(keyboard))


def callback_query_handler(update: telegram.Update, context: telegram.ext.CallbackContext):
    query = update.callback_query
    choice = query.data
    
    if choice == "answer":
        answer_handler(query)
    elif choice == "question":
        question_handler(query)


def main():
    print("initializing updater ...")
    updater = telegram.ext.Updater(TOKEN, use_context=True)
    
    print("initializing dispatcher ...")
    dispatcher = updater.dispatcher
    
    print("initializing command handlers ...")
    dispatcher.add_handler(telegram.ext.CommandHandler("start", start_command_handler))
    
    print("initializing callback query handlers ...")
    dispatcher.add_handler(telegram.ext.CallbackQueryHandler(callback_query_handler))
    
    print("starting poll ...")
    updater.start_polling()
    
    print("being idle ...")
    updater.idle()


main()
