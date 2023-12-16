import telebot
import random
from info import name_text, poiavlenie_text, who_you_are_text, audio2, audio1, audio3, start_audio, i_cant_audio, help_audio, hi_audio, buy_audio
from telebot import types
TOKEN = "6403240146:AAHENKywbBZPPWQPG6Iv26L33CQ-HkfycW4"
bot = telebot.TeleBot(TOKEN)
bot_responses = {
    "привет": ["Привет", "Здравствуйте", "Здорово", "Приветствую", "Рад видеть Вас"],
    "Как тебе?": ["Норма", "Превосходно, всегда бы вам так выглядеть",
                  "Купите новый телефон! Камера явно замылилась!", "Красивенько!", "Какое красивое фото!"],
    "пока": ["До свидания", "Пока", "До встречи", "Удачи вам! Я побежал творить дела"]
}

answer = random.choice(bot_responses["привет"])
answer2 = random.choice(bot_responses["Как тебе?"])
answer3 = random.choice(bot_responses["пока"])

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, f"Доброго времени суток, {message.from_user.first_name}! Я инопланетянин, меня зовут Пол Ламинат! Я готов пообщаться с вами (конечно же через бота)! Для полного представления об общении с инопланетной цивилизацией зайдите в бортовой журнал /help")
    bot.send_audio(message.chat.id, start_audio)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.send_message(message.chat.id, answer2)

@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    bot.send_message(message.chat.id, "К сожалению я не понимаю разговорную речь, но писать я толком научился, но не навсе вопросы могу дать ответ, загляни в бортовой журнал /help")
    bot.send_audio(message.chat.id, i_cant_audio)

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "/n - выводит имя"
                                      " /h - выводит историю появления на Земле"
                                      " /c - рассказывает о герое, /p - фото героя также можно спросить у бота  как дела (ДЕЛА в запросе). И сказать ПРИВЕТ и ПОКА  и получить ответ, рандомное оценивавине ваших фото!")
    bot.send_audio(message.chat.id, help_audio)

@bot.message_handler(commands=['p'])
def ooo(message):
    bot.send_photo(message.chat.id, open("C:\\Users\\USER\\Desktop\\jjjjjjj.jpg", "rb"))
@bot.message_handler(commands=["n"])
def bbb(message):
    knopka = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Имя будет в виде текста", callback_data='text_answer1')
    btn2 = types.InlineKeyboardButton("Имя будет в виде гс", callback_data='voice_answer2')
    knopka.row(btn1, btn2)
    bot.send_message(message.chat.id, "Выбирай!)", reply_markup=knopka)


@bot.message_handler(commands=["h"])
def ссс(message):
    knopka = types.InlineKeyboardMarkup()
    btn3 = types.InlineKeyboardButton("История будет в виде текста", callback_data='text_answer3')
    btn4 = types.InlineKeyboardButton("История будет в виде гс", callback_data='voice_answer4')
    knopka.row(btn3, btn4)
    bot.send_message(message.chat.id, "Выбирай!)", reply_markup=knopka)


@bot.message_handler(commands=['c'])
def vvv(message):
    knopka = types.InlineKeyboardMarkup()
    btn5 = types.InlineKeyboardButton("Характеристика будет в виде текста", callback_data='text_answer5')
    btn6 = types.InlineKeyboardButton("Характеристика будет в виде гс", callback_data='voice_answer6')
    knopka.row(btn5, btn6)
    bot.send_message(message.chat.id, "Выбирай!)", reply_markup=knopka)

@bot.message_handler(content_types=['text'])
def privet(messsge):
    if "привет" in messsge.text.lower():
        bot.send_message(messsge.chat.id, f"{answer}, {messsge.from_user.first_name}")
        bot.send_audio(messsge.chat.id, hi_audio)
    elif "пока" in messsge.text.lower():
        bot.send_message(messsge.chat.id, f'{answer3}!')
        bot.send_audio(messsge.chat.id, buy_audio)
    elif "дела" in messsge.text.lower():
        knopka = types.InlineKeyboardMarkup()
        btn7 = types.InlineKeyboardButton("⭐", callback_data='answer1')
        btn8 = types.InlineKeyboardButton("⭐🌟", callback_data='answer2')
        btn9 = types.InlineKeyboardButton("⭐🌟⭐", callback_data='answer3')
        btn10 = types.InlineKeyboardButton("⭐🌟⭐🌟", callback_data='answer4')
        btn11 = types.InlineKeyboardButton("⭐🌟⭐🌟⭐", callback_data='answer5')
        knopka.row(btn7, btn8)
        knopka.row(btn9, btn10)
        knopka.row(btn11)
        bot.send_message(messsge.chat.id, f"У меня как всегда лучше всех! А у вас {messsge.from_user.first_name}?(Выберите колличество звезд для оценки настроения)(сообщения бота не озвучиваются)", reply_markup=knopka)

    else:
        bot.send_message(messsge.chat.id, "Я вас не понял, обратитесь в /help)")

@bot.callback_query_handler(func=lambda callback: True)
def callback(callback):
    if callback.data == 'text_answer5':
        bot.send_message(callback.message.chat.id, who_you_are_text)
    elif callback.data == 'voice_answer6':
        bot.send_audio(callback.message.chat.id, audio3)
    elif callback.data == 'text_answer1':
        bot.send_message(callback.message.chat.id, name_text)
    elif callback.data == 'voice_answer2':
        bot.send_audio(callback.message.chat.id, audio1)
    elif callback.data == 'text_answer3':
        bot.send_message(callback.message.chat.id, poiavlenie_text)
    elif callback.data == 'voice_answer4':
        bot.send_audio(callback.message.chat.id, audio2)
    elif callback.data == "answer1":
        bot.send_message(callback.message.chat.id, "НЕ расстраивайтесь, надеюсь после разговора со мной вам станет легче!")
    elif callback.data == "answer1":
        bot.send_message(callback.message.chat.id, "Жизнь вообще тяжелая штука, но не отчаивайтесь!")
    elif callback.data == "answer2":
        bot.send_message(callback.message.chat.id, "НЕ расстраивайтесь, надеюсь после разговора со мной вам станет легче!")
    elif callback.data == "answer3":
        bot.send_message(callback.message.chat.id, "НЕ надо драматизировать, все хорошо, соберитесь!")
    elif callback.data == "answer4":
        bot.send_message(callback.message.chat.id, "Ну вот, хоть один человек у которого все хорошо!")
    elif callback.data == "answer5":
        bot.send_message(callback.message.chat.id, "Это конечно хорошо, но не надо тут расплываться в улыбке, как говорил технолог: Не известно когда на вас шкаф упадет) ")


bot.polling()





