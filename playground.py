import os
import dotenv
import telegram.ext

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")


def start_command_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    update.message.reply_text("Hello, friend!")


def help_command_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    update.message.reply_text("""
List of all commands:

/start - Start the bot
/help - Show the help message containing list of all commands
/about - Show the about message containing author information
    """)


def about_command_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    update.message.reply_text("Developed by @BijanProgrammer")


def hello_message_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    print(update)
    print(context)
    
    user = update.message.from_user
    
    first_name = user.first_name or ''
    last_name = user.last_name or ''
    username = user.username or ''
    
    if first_name != '':
        if last_name != '':
            update.message.reply_text(f"Hello, {first_name} {last_name}!")
        else:
            update.message.reply_text(f"Hello, {first_name}!")
    elif username != '':
        update.message.reply_text(f"Hello, {username}!")
    else:
        update.message.reply_text("Hello, friend!")


def math_command_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    first_number = float(context.args[0])
    operator = context.args[1]
    second_number = float(context.args[2])
    
    result = "<NOT IMPLEMENTED>"
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        result = first_number / second_number
    
    update.message.reply_text(f"{result:.2f}")


def main():
    print("initializing updater ...")
    updater = telegram.ext.Updater(TOKEN, use_context=True)
    
    print("initializing dispatcher ...")
    dispatcher = updater.dispatcher
    
    print("initializing command handlers ...")
    dispatcher.add_handler(telegram.ext.CommandHandler("start", start_command_handler))
    dispatcher.add_handler(telegram.ext.CommandHandler("help", help_command_handler))
    dispatcher.add_handler(telegram.ext.CommandHandler("about", about_command_handler))
    dispatcher.add_handler(telegram.ext.CommandHandler("math", math_command_handler))
    
    print("initializing message handlers ...")
    dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, hello_message_handler))
    
    print("starting poll ...")
    updater.start_polling()
    
    print("being idle ...")
    updater.idle()


main()
