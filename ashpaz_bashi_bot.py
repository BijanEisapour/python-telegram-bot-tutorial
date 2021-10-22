import json
import os
import dotenv
import telegram.ext
import requests

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")


def start_command_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    buttons = [
        [
            telegram.KeyboardButton("ایرانی 🇮🇷"),
            telegram.KeyboardButton("سوپ و آش 🍲"),
        ],
        [
            telegram.KeyboardButton("ایتالیایی 🇮🇹"),
            telegram.KeyboardButton("فست فود 🍔"),
        ],
        [
            telegram.KeyboardButton("پیتزا 🍕"),
            telegram.KeyboardButton("کیک و شیرینی 🧁"),
        ],
    ]
    
    message = "یکی از دسته‌بندی‌های زیر را انتخاب کنید ..."
    reply_markup = telegram.ReplyKeyboardMarkup(buttons, one_time_keyboard=True)
    
    update.effective_message.reply_text(message, reply_markup=reply_markup)


def tag_message_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    tag = update.message.text[:-2]
    response = requests.get(f"http://localhost:5000/tag/{tag}/1").json()
    
    if "error" in response:
        update.message.reply_text(response['error'])
        return
    
    callback_data = f"t_{tag}_1"
    
    keyboard = [
        [
            telegram.InlineKeyboardButton("🍗 لیست غذاها 🍗",
                                          callback_data=callback_data),
        ],
    ]
    
    content = f"برای نمایش غذاهای دسته‌بندی {tag} لطفاً برروی دکمۀ زیر بزنید ..."
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    update.message.reply_text(content, reply_markup=reply_markup)


def tag_pager(query: telegram.CallbackQuery, tag: str, page: int) -> None:
    response = requests.get(f"http://localhost:5000/tag/{tag}/{page}").json()
    
    keyboard = [
        []
    ]
    
    if response["prev"]:
        callback_data = f"t_{tag}_{page - 1}"
        keyboard[0].append(telegram.InlineKeyboardButton("صفحۀ قبل 👈", callback_data=callback_data))
    
    if response["next"]:
        callback_data = f"t_{tag}_{page + 1}"
        keyboard[0].append(telegram.InlineKeyboardButton("👉 صفحۀ بعد", callback_data=callback_data))
    
    food_groups = [response["foods"][offset:offset + 3] for offset in range(0, len(response["foods"]), 3)]
    
    for group in food_groups:
        buttons = []
        for food in group:
            callback_data = f"f_{food}"
            buttons.append(telegram.InlineKeyboardButton(food, callback_data=callback_data))
        
        keyboard.append(buttons)
    
    content = f"لیست غذاهای دسته‌بندی {tag} ..."
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(content, reply_markup=reply_markup)


def show_recipe(query: telegram.CallbackQuery, food: str) -> None:
    response = requests.get(f"http://localhost:5000/food/{food}").json()
    
    if "error" in response:
        query.message.reply_text(response['error'])
        return
    
    reply_markup = telegram.ReplyKeyboardRemove()
    
    first_message_content = f"""
نام: {response['recipe']['title']}
برچسب‌ها: {", ".join(response['recipe']['tags'])}
زمان تهیه: {response['recipe']['preparationTime']}
زمان طبخ: {response['recipe']['cookTime']}
    """
    
    second_message_content = ""
    for ingredient in response['recipe']['ingredients']:
        second_message_content += f"{ingredient['title']}: {ingredient['amount']}\n"
    
    third_message_content = "\n\n".join(response['recipe']['steps'])
    
    query.message.reply_text(first_message_content, reply_markup=reply_markup)
    query.message.reply_text(second_message_content, reply_markup=reply_markup)
    query.message.reply_text(third_message_content, reply_markup=reply_markup)


def callback_query_handler(update: telegram.Update, context: telegram.ext.CallbackContext):
    query = update.callback_query
    choice = query.data
    
    parts = choice.split("_")
    
    if parts[0] == "t":
        tag_pager(query, parts[1], int(parts[2]))
    elif parts[0] == "f":
        show_recipe(query, parts[1])


def main():
    print("initializing updater ...")
    updater = telegram.ext.Updater(TOKEN, use_context=True)
    
    print("initializing dispatcher ...")
    dispatcher = updater.dispatcher
    
    print("initializing command handlers ...")
    dispatcher.add_handler(telegram.ext.CommandHandler("start", start_command_handler))
    
    print("initializing message handlers ...")
    dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, tag_message_handler))
    
    print("initializing callback query handlers ...")
    dispatcher.add_handler(telegram.ext.CallbackQueryHandler(callback_query_handler))
    
    print("starting poll ...")
    updater.start_polling()
    
    print("being idle ...")
    updater.idle()


main()
