import random
import telebot
from bot_logic import gen_pass
from telebot.types import ReactionTypeEmoji
import os




API_TOKEN = '8473665011:AAEAjIJmNp4-79ielfqwBxarrbQgZzFxBVY'
bot = telebot.TeleBot("8473665011:AAEAjIJmNp4-79ielfqwBxarrbQgZzFxBVY")

bot.message_handler(commands=['help'])  
def handle_help(message):  
    help_text = ("/start — Начать работу с ботом\n" "/help — Получить список команд\n")  
    bot.send_message(message.chat.id, help_text)  
    with open('images/eco_1.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

text_messages = {
    'welcome':
        u'Please welcome {name}!\n\n'
        u'This chat is intended for questions about and discussion of the pyTelegramBotAPI.\n'
        u'To enable group members to answer your questions fast and accurately, please make sure to study the '
        u'project\'s documentation (https://github.com/eternnoir/pyTelegramBotAPI/blob/master/README.md) and the '
        u'examples (https://github.com/eternnoir/pyTelegramBotAPI/tree/master/examples) first.\n\n'
        u'I hope you enjoy your stay here!',

    'info':
        u'My name is TeleBot,'
        u'I am a bot that can help you start living a sustainable life.'
        u'Also, I am still under development. Please improve my functionality by making a pull request!'
        u'Suggestions are also welcome, just drop them in this group chat!',
        u'Here are some commands that will help you understand: /eco_plan, /sorting_garbage, /ideas'

    'wrong_chat':
        u'Hi there!\nThanks for trying me out. However, this bot can only be used in the pyTelegramAPI group chat.\n'
        u'Join us!\n\n'
        u'https://telegram.me/joinchat/067e22c60035523fda8f6025ee87e30b'
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Мое имя  ТелеБот,\n"
    u"Кроме того, я все еще нахожусь в стадии разработки. Пожалуйста, улучшите мою функциональность, отправив запрос на обновление!\n"
    u"Предложения также приветствуются, просто оставляйте их в этом групповом чате!\n"
    u"/eco_plan, /sorting_garbage, /ideas")
    with open('images/eco_1.jpg', 'rb') as f:  
      bot.send_photo(message.chat.id, f)



@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['eco_plan'])
def send_eco_plan(message):
    bot.reply_to(message, "План по уменьшению отходов для подростка:\n"
    u"1. Понять, зачем это нужно\n"
    u"2. Оценить текущую ситуацию\n"
    u"3. Начать с малого\n"
    u"4. Разделяйте отходы правильно\n"
    u"5. Вовлекайте друзей и семью\n"
    u"6. Учитесь и вдохновляйтесь")
    with open('images/eco_2.jpg', 'rb') as f:  
      bot.send_photo(message.chat.id, f)




@bot.message_handler(commands=['sorting_garbage'])
def sorting_garbage(message):
    bot.reply_to(message, '- Откажитесь от одноразового пластика: используйте многоразовые бутылки и сумки.\n'
u'- Снизьте использование упаковок и выбирайте товары в упаковке, которую можно переработать.\n'
u'- Откажитесь от ненужных покупок — подумайте, действительно ли вещь нужна.')
    with open('images/eco_3.jpg', 'rb') as f:  
      bot.send_photo(message.chat.id, f)



@bot.message_handler(commands=['ideas'])
def ides(message):
    bot.reply_to(message, 'Несколько идей для того чтобы добиться плана:'
    u'Посмотрите, сколько и каких отходов вы производите дома. Можно вести дневник или сделать фото мусорных пакетов на неделю.'
    u'Научитесь сортировать мусор дома: бумага, пластик, стекло, органика. Это помогает переработке.'
    u'Расскажите близким о своих целях, вместе будет легче и интереснее.'
    u'Читайте статьи, смотрите видео на тему zero waste, следите за блогерами, которые делятся опытом уменьшения отходов.')
    with open('images/eco_1.jpg', 'rb') as f:  
      bot.send_photo(message.chat.id, f)





@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")


@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)



@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")



@bot.message_handler(commands=['info'])
def on_info(message):
    bot.reply_to(message, text_messages['info'])


# @bot.message_handler(func=lambda message: True)
# def send_reaction(message):
#     emo = ["\U0001F525", "\U0001F917", "\U0001F60E"]  # or use ["🔥", "🤗", "😎"]
#     bot.set_message_reaction(message.chat.id, message.id, [ReactionTypeEmoji(random.choice(emo))], is_big=False)


#@bot.message_handler(commands=['mem'])
#with open('images/mem1.jpeg', 'rb') as f:  
     # bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['random_mem'])
def send_random_mem(message):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

bot.polling()
