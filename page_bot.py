import os
import dotenv
import telegram.ext

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")


def start_command_handler(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    keyboard = [
        [
            telegram.InlineKeyboardButton("📖 START READING 📖", callback_data='1'),
        ],
    ]
    
    content = """🔸 Cover
    
First star I see tonight
by Andrew Leon Hudson and adapted by Nicola Prentis
    """
    
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(content, reply_markup=reply_markup)


def page_1_handler(query: telegram.CallbackQuery) -> None:
    keyboard = [
        [
            telegram.InlineKeyboardButton("Page 2 👉", callback_data='2'),
        ],
    ]
    
    content = """🔸 Page 1
    
Dr Tomas Streyer looked around the control room at his team of scientists and engineers. He was excited and frightened but he tried to seem calm. In a few minutes, they might start to discover something amazing: how the universe began.

He looked out of the window at the beautiful blue summer sky and tried to breathe slowly.

'Ready,' he said. He pressed the first button and the complicated computers and machines came to life.

'Set,' he said. He pressed the second button and switched on the large particle accelerator that lay under the towns and fields of Switzerland.

'Go,' he said. And, at exactly twelve o'clock, he pressed the final button.

For a second, he felt as if he was blind, because everything went completely black. Tomas shouted in shock, but the lights were already on again. That was not part of his plan. He had no idea what had just happened.

'Everybody, check the systems!' he ordered. But nothing seemed to be wrong with them. The particle accelerator was working perfectly.

'Tomas,' said his assistant. 'Look outside.' She sounded afraid.
    """
    
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(content, reply_markup=reply_markup)


def page_2_handler(query: telegram.CallbackQuery) -> None:
    keyboard = [
        [
            telegram.InlineKeyboardButton("👈 Page 1", callback_data='1'),
            telegram.InlineKeyboardButton("Page 3 👉", callback_data='3'),
        ],
    ]
    
    content = """🔸 Page 2
    
The perfect summer's day of five minutes ago had gone. Instead, the sky was darker than the blackest night. But that wasn't the worst thing. The sun wasn't there, and the moon and stars were also gone.

People were shouting and screaming. They started calling their families on the telephone because they were afraid they had all gone too. Tomas felt as if it was hard to breathe, but he counted to ten and tried to breathe slowly. He sat at the main computer and started reading the information and numbers from his experiment. But he couldn’t find anything to explain what was happening. He ran out of the exit with the rest of his team until they were all outside the building.

Everyone else in the building was outside, frightened and confused. They were using the screens and lights on their mobile phones to see better. Several people got in their cars and turned on the lights. They drove to the entrance to make a small area of light for everybody to stand together. The street lights turned on, but most people were still afraid.

Then, almost twenty minutes after Tomas had started the particle accelerator, the sun was in the sky again. It was warm and yellow, and the black sky turned blue again. Everyone started laughing and dancing around, and Tomas felt as if he could breathe normally again.

But later, hours later, when the real night began, no one was happy. Because, although the moon rose again, there were no stars in the sky at all.
    """
    
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(content, reply_markup=reply_markup)


def page_3_handler(query: telegram.CallbackQuery) -> None:
    keyboard = [
        [
            telegram.InlineKeyboardButton("👈 Page 2", callback_data='2'),
            telegram.InlineKeyboardButton("Page 4 👉", callback_data='4'),
        ],
    ]
    
    content = """🔸 Page 3
    
No one wanted to know what Tomas' work was actually about. They didn't care what the particle accelerator was for. What did that matter? All they cared about was what had happened after he turned the machine on. He had stolen all the stars – or that's what the newspapers said. And when they made him go to the International Criminal Court, they charged him with stealing the stars.

Tomas said, 'I'm not guilty.'

'Well, if you didn’t steal the stars, Dr Streyer,' said the lawyer for the prosecution, 'what did you do?'

'If you're asking about my work,' said Tomas, 'we didn't do anything. We showed that the machine was working, that's all.'

'Taking the stars from the sky seems like nothing to you?' The lawyer looked around at the people in the court. 'No one here would think it's nothing. No one in the world would think it's nothing.'

'That's not what I meant,' said Tomas. 'But I can tell you this: when the machine started, there were suddenly no photons in the test room.'

'What? Photons? We aren't all scientists here! Speak simple English, Dr Streyer!'

'Light,' said Tomas. 'For just a moment it was as if there was no light in our laboratory. Then we saw it was also dark outside … until the light became normal again.'

'Normal, Dr Streyer? It wasn't normal when …' – the lawyer checked his notes – '… the sun went out for exactly sixteen minutes and forty seconds. Perhaps we can say the rest of the day was normal. But the night hasn't been normal ever since, has it?'
    """
    
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(content, reply_markup=reply_markup)


def page_4_handler(query: telegram.CallbackQuery) -> None:
    keyboard = [
        [
            telegram.InlineKeyboardButton("👈 Page 3", callback_data='3'),
            telegram.InlineKeyboardButton("Page 5 👉", callback_data='5'),
        ],
    ]
    
    content = """🔸 Page 4
    
Tomas looked sad. 'I know. But you must believe me. I didn't do anything that could have taken the stars from the sky!'

'So are you saying you didn't steal the stars from us?' said the lawyer.

'No, I didn't steal them,' Tomas said.

'You just made it so that we can't see them any more.'

After a long pause, Tomas spoke. 'Yes,' he said.

'How is that any different?' the lawyer asked.

Tomas didn't have an answer, not one anyone would understand anyway. And if they understood it, they wouldn't believe him. He had an idea, but it would take years to prove it.

Instead, he changed his mind and said, 'I'm guilty.'
    """
    
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(content, reply_markup=reply_markup)


def page_5_handler(query: telegram.CallbackQuery) -> None:
    keyboard = [
        [
            telegram.InlineKeyboardButton("👈 Page 4", callback_data='4'),
            telegram.InlineKeyboardButton("Page 6 👉", callback_data='6'),
        ],
    ]
    
    content = """🔸 Page 5
    
Now the world could blame someone for what it had lost. But there was no point sending Tomas to prison for years. It wouldn't change anything. Instead, they designed a punishment especially for him.

They sent Tomas to work at the Extremely Large Telescope in Paranal in Chile. Nobody used the telescope now. No tourists came to these high mountains to see the edges of our galaxy. No scientists asked for money to study the empty sky. All that passed through the night sky was the lonely moon and a few planets. Looking up made people feel bad.

Tomas thought it was fair that they punished him. And the job was almost the same as prison because he was completely alone. After a few years, the world forgot about him. Or, at least, everyone decided to leave him alone. Every evening he watched the sun go down. The red ball was gone exactly eight minutes and twenty seconds after it actually went behind the Earth. Tomas was almost happy to know that the laws of physics remained the same. Light still travelled at the same speed as it had always travelled. He hoped it meant he hadn't changed the universe that much. We know there is a speed light travels at, he thought, so perhaps the dark travels at the same speed.

Of course, there was no way to prove his idea. Not yet. And, alone in the mountains, Tomas had nobody to share his idea with anyway.
    """
    
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(content, reply_markup=reply_markup)


def page_6_handler(query: telegram.CallbackQuery) -> None:
    keyboard = [
        [
            telegram.InlineKeyboardButton("👈 Page 5", callback_data='5'),
            telegram.InlineKeyboardButton("Page 7 👉", callback_data='7'),
        ],
    ]
    
    content = """🔸 Page 6
    
High in the mountains of Chile, Tomas continued to watch the night sky. With the enormous telescope, he looked at the same place in the empty sky every night, even though there was nothing to see. And each day as the sun went down, he thought of the song his parents sang to him as a child:



Star light, star bright,
First star I see tonight,
I wish I may, I wish I might,
Have the wish I wish tonight.



For 1,596 black nights – nearly four and a half years – there was no change to the night sky. But that was OK. It didn't mean his idea was wrong. Tomas thought about the darkness he had created. He imagined it like a wave that had passed the sun. Now, maybe, it was continuing out towards the edge of our galaxy and further, to the stars. It would take 1,596 nights to pass the nearest star. It would take 1,596 more nights for that star's light to come back to Earth ... If the wave was real, of course. If his ideas were correct. If he was wrong, the stars were really gone forever.
    """
    
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(content, reply_markup=reply_markup)


def page_7_handler(query: telegram.CallbackQuery) -> None:
    keyboard = [
        [
            telegram.InlineKeyboardButton("👈 Page 6", callback_data='6'),
        ],
    ]
    
    content = """🔸 Page 7
    
And then one night 1,596 nights later, almost nine years after that terrible day, Tomas looked up from his telescope. There was Alpha Centauri twinkling back at him from the night sky.

The first star.

He felt tears in his eyes and he made a wish. And he imagined millions of other people were making their wishes too.



Story written by Andrew Leon Hudson and adapted by Nicola Prentis.
    """
    
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(content, reply_markup=reply_markup)


def callback_query_handler(update: telegram.Update, context: telegram.ext.CallbackContext):
    query = update.callback_query
    choice = query.data
    
    if choice == "1":
        page_1_handler(query)
    elif choice == "2":
        page_2_handler(query)
    elif choice == "3":
        page_3_handler(query)
    elif choice == "4":
        page_4_handler(query)
    elif choice == "5":
        page_5_handler(query)
    elif choice == "6":
        page_6_handler(query)
    elif choice == "7":
        page_7_handler(query)


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
