from get_info import *
import telebot
from auth_data import token


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Работаем")
        # Functions to open webpages for search
        enter_web_page()

    @bot.message_handler(commands=['loop'])
    def loop_message(message):
        while True:
            bot.send_message(message.chat.id, "Открываем окно ...")
            click_open()
            time.sleep(120)
            bot.send_message(message.chat.id, "Ищем новые сообщения ...")
            all_list = check_all()
            for item in all_list:
                bot.send_message(message.chat.id, f"{item}")
                print(item)
            time.sleep(120)


    @bot.message_handler(content_types=['text'])
    def send_text(message):

        if message.text.lower() == 'f':
            bot.send_message(message.chat.id, "Ищем нужный заказ ...")
            drain_list = check_drain()
            for item in drain_list:
                bot.send_message(message.chat.id, f"{item}")
                print(item)

        elif message.text.lower() != 'o':
            bot.send_message(message.chat.id, "Код принят")
            enter_code(message.text)
            enter_chat()

    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            time.sleep(60)


if __name__ == "__main__":
    telegram_bot(token=token)
