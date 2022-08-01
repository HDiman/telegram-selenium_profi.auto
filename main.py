from get_info import *
import telebot
from auth_data import token
import re


def validate_pin(pin):
    if re.search('^\d{4}$', pin):
        return True
    else:
        return False

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['loop'])
    def loop_message(message):
        while True:
            try:
                bot.send_message(message.chat.id, "Открываем окно ...")
                click_open()
                time.sleep(3)
                bot.send_message(message.chat.id, "Список заказов в окне:")
                all_list = check_all()
                if all_list == []:
                    bot.send_message(message.chat.id, "Заказов нет")
                else:
                    for item in all_list:
                        bot.send_message(message.chat.id, f"{item}")
                        print(item)
                time.sleep(57)
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Error in loop!")

    @bot.message_handler(commands=['stop'])
    def loop_message(message):
        while True:
            try:
                bot.send_message(message.chat.id, "... Ожидаем указа ... ")
                time.sleep(60000)
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Error in stop!")

    @bot.message_handler(commands=['start'])
    def start_message(message):
        try:
            bot.send_message(message.chat.id, "Начинаем")
            # Functions to open webpages for search
            enter_web_page()
        except Exception as ex:
            print(ex)
            bot.send_message(message.chat.id, "Error in start!")

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        try:
            if validate_pin(message.text.lower()):
                bot.send_message(message.chat.id, "Код принят")
                enter_code(message.text)
                enter_chat()
                bot.send_message(message.chat.id, "Можно работать")
            else:
                bot.send_message(message.chat.id, "Повторите ввод")
        except Exception as ex:
            print(ex)
            bot.send_message(message.chat.id, "Error in text!")

    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            time.sleep(60)


if __name__ == "__main__":
    telegram_bot(token=token)
