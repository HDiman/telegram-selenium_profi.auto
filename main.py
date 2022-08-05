from get_info import *
import telebot
from auth_data import token
import re


def validate_pin(pin):
    if re.search('^\d{4}$', pin):
        return True
    else:
        return False

def validate_time(time_enter):
    if re.search('^\d{1,2}$', time_enter):
        return True
    else:
        return False


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        try:
            bot.send_message(message.chat.id, "Начинаем работу Т-О-Т-Е")
            # Functions to open webpages for search
            enter_web_page()
        except Exception as ex:
            print(ex)
            bot.send_message(message.chat.id, "Error in start!")

    @bot.message_handler(content_types=['text'])
    def send_text(message):

        # Function for looping num times
        def looping(num):
            for i in range(num):
                try:
                    bot.send_message(message.chat.id, "+-----------------------------------------------------------+")
                    click_open()
                    time.sleep(3)
                    bot.send_message(message.chat.id, "Список заказов:")
                    all_list = check_all()
                    if all_list == []:
                        bot.send_message(message.chat.id, "Заказов нет")
                    else:
                        for item in all_list:
                            bot.send_message(message.chat.id, f"{item}")
                            print(item)
                    bot.send_message(message.chat.id, f"Осталось {num - (i + 1)} мин ...")
                    time.sleep(57)
                except Exception as ex:
                    print(ex)
                    bot.send_message(message.chat.id, "Error in loop!")
            bot.send_message(message.chat.id, "... Ожидаю команду ... ")

        try:
            if validate_pin(message.text):
                bot.send_message(message.chat.id, "Код принят")
                enter_code(message.text)
                enter_chat()
                bot.send_message(message.chat.id, "Введите время в минутах")
            elif validate_time(message.text):
                bot.send_message(message.chat.id, f"Время установлено на: {message.text} мин.")
                looping(int(message.text))

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
