import os
import dotenv
import telegram.ext

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")


def start_command_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    update.message.reply_text("Hello, friend!")


def keyboard_button_command_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    buttons = [
        [
            telegram.KeyboardButton("Option 1"),
            telegram.KeyboardButton("Option 2"),
        ],
        [telegram.KeyboardButton("Option 3")],
    ]
    
    message = "Choose one of the following ..."
    reply_markup = telegram.ReplyKeyboardMarkup(buttons)
    
    update.effective_message.reply_text(message, reply_markup=reply_markup)


def inline_keyboard_button_command_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    buttons = [
        [
            telegram.InlineKeyboardButton("Option 1", callback_data='1'),
            telegram.InlineKeyboardButton("Option 2", callback_data='2'),
        ],
        [telegram.InlineKeyboardButton("Option 3", callback_data='3')],
    ]
    
    message = "Choose one of the following ..."
    reply_markup = telegram.InlineKeyboardMarkup(buttons)
    
    update.message.reply_text(message, reply_markup=reply_markup)


def message_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    reply_markup = telegram.ReplyKeyboardRemove()
    update.message.reply_text("Done!", reply_markup=reply_markup)


def callback_query_handler(update: telegram.Update, context: telegram.ext.CallbackContext):
    query = update.callback_query
    
    # query.answer("this is an answer!")
    # query.message.reply_text("this is a reply_text!")
    query.edit_message_text(text=f"Selected option: {query.data}")


def main():
    print("initializing updater ...")
    updater = telegram.ext.Updater(TOKEN, use_context=True)
    
    print("initializing dispatcher ...")
    dispatcher = updater.dispatcher
    
    print("initializing command handlers ...")
    dispatcher.add_handler(telegram.ext.CommandHandler("start", start_command_handler))
    dispatcher.add_handler(telegram.ext.CommandHandler("keyboardbutton", keyboard_button_command_handler))
    dispatcher.add_handler(telegram.ext.CommandHandler("inlinekeyboardbutton", inline_keyboard_button_command_handler))
    
    print("initializing message handlers ...")
    dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, message_handler))
    
    print("initializing callback query handlers ...")
    dispatcher.add_handler(telegram.ext.CallbackQueryHandler(callback_query_handler))
    
    print("starting poll ...")
    updater.start_polling()
    
    print("being idle ...")
    updater.idle()


main()
