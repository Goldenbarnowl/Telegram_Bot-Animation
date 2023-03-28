#pip install openpyxl
#pip install pyTelegramBotAPI
#-----------------------------------------------------------------------------------


import telebot
from telebot import types
import time

#-----------------------------------------------------------------------------------


TOKEN = input("Введите токен бота>> ")
bot = telebot.TeleBot(TOKEN)
print("\nТокен введен успешно, бот активен!")
#-----------------------------------------------------------------------------------

@bot.message_handler(commands=['start'])
def welcome(message):
    if(("{0.last_name}".format(message.from_user, bot.get_me())) == "None"):
        print("{0.first_name} {0.last_name}".format(message.from_user, bot.get_me()))
        bot.send_message(message.chat.id,"Здравствуйте, {0.first_name}!\nБот создан для ознакомления с анимированными сообщениями.".format(message.from_user, bot.get_me()), parse_mode='html')
    elif (("{0.first_name}".format(message.from_user, bot.get_me())) == "None"):
        print("{0.first_name} {0.last_name}".format(message.from_user, bot.get_me()))
        bot.send_message(message.chat.id,"Здравствуйте, {0.last_name}!\nБот создан для ознакомления с анимированными сообщениями.".format(message.from_user, bot.get_me()), parse_mode='html')
    else:
        print("{0.first_name} {0.last_name}".format(message.from_user, bot.get_me()))
        bot.send_message(message.chat.id,"Здравствуйте!\nБот создан для ознакомления с анимированными сообщениями.".format(message.from_user, bot.get_me()), parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('❤️')
    item2 = types.KeyboardButton('⏳')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Выберите интересующую вас анимацию:'.format(message.from_user), reply_markup=markup)

#-----------------------------------------------------------------------------------

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':

        global bool
        bool = True
        if message.text == '❤️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('⬅️')

            markup.add(item1)

            bot.send_message(message.chat.id, 'Матрица из сердечек:'.format(message.from_user),reply_markup=markup)

            matrix = ["❤🧡💛💚💙💜", "🧡💛💚💙💜❤","💛💚💙💜❤🧡","💚💙💜❤🧡💛","💙💜❤🧡💛💚","💜❤🧡💛💚💙"]
            enter = "❤️🧡💛💚💙💜\n🧡💛💚💙💜❤️\n💛💚💙💜❤️🧡\n💚💙💜❤️🧡💛\n💙💜❤️🧡💛💚\n💜❤️🧡💛💚💙"
            botmessage = bot.send_message(message.chat.id, enter.format(message.from_user, bot.get_me()),parse_mode='html')
            while (bool):
                for x in range(6):
                    matrix[x] = matrix[x][5] + matrix[x][:-1]
                enter = ""
                for y in range(6):
                    enter+= "\n" + matrix[y]
                time.sleep(1)
                bot.edit_message_text(chat_id=message.chat.id, message_id=botmessage.message_id, text=enter)

        if message.text == '⏳':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('⬅️')

            markup.add(item1)

            bot.send_message(message.chat.id, 'Анимация загрузки:'.format(message.from_user), reply_markup=markup)

            text = "Loading..."
            proc = 10
            load = ["██", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒"]
            botmessage = bot.send_message(message.chat.id, "Loading...0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒".format(message.from_user, bot.get_me()),parse_mode='html')
            time.sleep(1)
            for y in range(1,11):
                loadtext = ""
                for x in range(10):
                    loadtext += load[x]
                enter = text + str(proc) + "%\n" + loadtext
                proc += 10
                load[y] = "██"
                bot.edit_message_text(chat_id=message.chat.id, message_id=botmessage.message_id, text = enter)
                time.sleep(1)
            bot.edit_message_text(chat_id=message.chat.id, message_id=botmessage.message_id, text="Loading  complet\n████████████████████".format(message.from_user, bot.get_me()))
            time.sleep(1)

        if message.text == '⬅️':
            bool = False
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('❤️')
            item2 = types.KeyboardButton('⏳')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Выберите интересующую вас анимацию:'.format(message.from_user),reply_markup=markup)
#-----------------------------------------------------------------------------------

bot.polling(none_stop=True)
