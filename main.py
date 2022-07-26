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

    @bot.message_handler(content_types=['text'])
    def send_text(message):

        if message.text.lower() == 'n':
            bot.send_message(message.chat.id, "Открываем окно сообщений")
            click_note()

        elif message.text.lower() == 't':
            bot.send_message(message.chat.id, "Ищем новые сообщения")
            inbox_text = inbox_orders()
            for i in range(len(inbox_text)):
                bot.send_message(message.chat.id, f"{inbox_text[i]}")
                print(inbox_text[i])

        elif message.text.lower() != 'o':
            bot.send_message(message.chat.id, "Код принят")
            enter_code(message.text)
            enter_chat()

        elif message.text.lower() == 'o':
            try:

                # OPEN ORDERS Section
                open_temp = open_orders()

                if open_temp == []:
                    bot.send_message(message.chat.id, "-- Нет ордеров: -- ОТКРЫТЫЕ --")
                    print("-- Нет ордеров: -- ОТКРЫТЫЕ --")
                else:
                    for n in range(len(open_temp)):

                        # Text for search in Youtube
                        search_open = open_temp[n]['марка:'] + " " + open_temp[n]['проблема:']
                        search_open = search_open.split('.')[0]

                        # Taking all text about an order in one message
                        open_temp_2 = list(open_temp[n].items())
                        open_temp_3 = ''
                        for item in open_temp_2:
                            tpl = " ".join(item)
                            open_temp_3 = open_temp_3 + tpl + '\n'

                        # Printing info about order in one message
                        bot.send_message(message.chat.id, f"{open_temp_3}")
                        print(open_temp_3)

                        # Text for searching in youtube
                        bot.send_message(message.chat.id, f"{search_open}")
                        print(search_open)


                # WORKING ORDERS Section
                working_temp = working_orders()

                if working_temp == []:
                    bot.send_message(message.chat.id, "-- Нет ордеров: -- В РАБОТЕ --")
                    print("-- Нет ордеров: -- В РАБОТЕ --")
                else:
                    for n in range(len(working_temp)):
                        # Text for search in Youtube
                        search_working = working_temp[n]['марка:'] + " " + working_temp[n]['проблема:']
                        search_working = search_working.split('.')[0]

                        # Taking all text about an order in one message
                        working_temp_2 = list(working_temp[n].items())
                        working_temp_3 = ''
                        for item in working_temp_2:
                            tpl = " ".join(item)
                            working_temp_3 = working_temp_3 + tpl + '\n'

                        # Printing info about order in one message
                        bot.send_message(message.chat.id, f"{working_temp_3}")
                        print(working_temp_3)

                        # Text for searching in youtube
                        bot.send_message(message.chat.id, f"{search_working}")
                        print(search_working)


            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Error!")
        else:
            bot.send_message(message.chat.id, "I like myself!")
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            time.sleep(60)


if __name__ == "__main__":
    telegram_bot(token=token)