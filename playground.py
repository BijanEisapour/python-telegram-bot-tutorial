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
            update.message.reply_text(f"Hello, [{first_name} {last_name}](tg://user?id={user.id})!",
                                      parse_mode=telegram.ParseMode.MARKDOWN)
        else:
            update.message.reply_text(f"Hello, {first_name}!")
    elif username != '':
        update.message.reply_text(f"Hello, {username}!")
    
    update.message.reply_text(f"Hello, [friend](tg://user?id={user.id})!",
                              parse_mode=telegram.ParseMode.MARKDOWN)


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


def bold_command_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    text = " ".join(context.args)
    
    update.message.reply_text(f"*{telegram.utils.helpers.escape_markdown(text)}*",
                              parse_mode=telegram.ParseMode.MARKDOWN)


def italic_command_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    text = " ".join(context.args)
    
    update.message.reply_text(f"_{telegram.utils.helpers.escape_markdown(text)}_",
                              parse_mode=telegram.ParseMode.MARKDOWN)


def monospace_command_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    text = " ".join(context.args)
    
    result = f"""
```
{text}
```
"""
    
    update.message.reply_text(result, parse_mode=telegram.ParseMode.MARKDOWN)


def inline_query_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    print(update)
    query = update.inline_query.query
    
    if query == "":
        return
    
    results = [
        telegram.InlineQueryResultArticle(
            id="1",
            title="Caps",
            input_message_content=telegram.InputTextMessageContent(query.upper()),
        ),
        telegram.InlineQueryResultArticle(
            id="2",
            title="Bold",
            input_message_content=telegram.InputTextMessageContent(
                f"*{telegram.utils.helpers.escape_markdown(query)}*", parse_mode=telegram.ParseMode.MARKDOWN
            ),
        ),
        telegram.InlineQueryResultArticle(
            id="3",
            title="Italic",
            input_message_content=telegram.InputTextMessageContent(
                f"_{telegram.utils.helpers.escape_markdown(query)}_", parse_mode=telegram.ParseMode.MARKDOWN
            ),
        ),
    ]
    
    update.inline_query.answer(results)


def reply_message_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    update.message.reply_text("@BijanProgrammer", reply_to_message_id=update.message.message_id)


def forward_message_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    context.bot.forward_message(chat_id=update.message.chat_id, from_chat_id=update.message.chat_id,
                                message_id=update.message.message_id)


def photo_command_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    context.bot.send_photo(update.message.chat_id, photo=open("./assets/photo.jpg", 'rb'))
    context.bot.send_photo(update.message.chat_id,
                           "https://via.placeholder.com/150/1aaaaa/fafafa?Text=This+is+a+sample+text")


def sticker_command_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    context.bot.send_sticker(chat_id=update.message.chat_id,
                             sticker='CAACAgIAAxkBAAM7YXGEbabBdFjAdII5NmaMJJ-PfSoAAvcAA1advQoLciQdSPQNMCEE')


def sticker_message_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    update.message.reply_text(update.message.sticker.file_id)


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
    dispatcher.add_handler(telegram.ext.CommandHandler("bold", bold_command_handler))
    dispatcher.add_handler(telegram.ext.CommandHandler("italic", italic_command_handler))
    dispatcher.add_handler(telegram.ext.CommandHandler("monospace", monospace_command_handler))
    dispatcher.add_handler(telegram.ext.CommandHandler("photo", photo_command_handler))
    dispatcher.add_handler(telegram.ext.CommandHandler("sticker", sticker_command_handler))
    
    print("initializing message handlers ...")
    # dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, hello_message_handler))
    # dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, reply_message_handler))
    # dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, forward_message_handler))
    dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.sticker, sticker_message_handler))
    
    print("initializing inline query handlers ...")
    dispatcher.add_handler(telegram.ext.InlineQueryHandler(inline_query_handler))
    
    print("starting poll ...")
    updater.start_polling()
    
    print("being idle ...")
    updater.idle()


main()
