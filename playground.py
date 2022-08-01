import requests
import telebot
from auth_data import token
import time
import schedule
from telebot import types


def get_data():
    # s_city = "Moscow,RU"
    # city_id = 524901
    # appid = key
    try:
        # res = requests.get("http://api.openweathermap.org/data/2.5/weather",
        #                    params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        # data = res.json()
        # weather = data['main']['temp']
        # cond = data['weather'][0]['description']
        # min_t = data['main']['temp_min']
        # max_t = data['main']['temp_max']
        #
        # print("conditions:", data['weather'][0]['description'])
        # print("temp:", data['main']['temp'])
        # print("temp_min:", data['main']['temp_min'])
        # print("temp_max:", data['main']['temp_max'])
        return [1, 2, 3,4]
    except Exception as e:
        print("Exception (weather):", e)
        pass

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def selfmyself(message):
        service = telebot.types.ReplyKeyboardMarkup(True, True)
        service.row('Wunderlist')
        service.row('Telegraph')
        service.row('Погода')
        bot.send_message(message.from_user.id, 'Что будем делать?', reply_markup=service)


    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        if message.text == "Wunderlist":
            a = telebot.types.ReplyKeyboardRemove()
            bot.send_message(message.from_user.id, 'Что', reply_markup=a)


    @bot.message_handler(commands=['loop'])
    def loop_message(message):
        while True:
            bot.send_message(message.chat.id, f"temp: {get_data()[0]}\n"
                                              f"condition: {get_data()[1]}\n")
            time.sleep(10)

    # @bot.message_handler(commands=['start'])
    # def start_message(message):
    #     markup = types.InlineKeyboardMarkup()
    #     markup.add(types.InlineKeyboardButton("Yandex", url="https://yabdex.ru"))
    #     bot.send_message(message.chat.id, "Visit site", reply_markup=markup)

    @bot.message_handler(commands=['help'])
    def start_message(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        website = types.KeyboardButton("Website")
        start = types.KeyboardButton("Start")
        markup.add(website, start)
        bot.send_message(message.chat.id, "Help is made", reply_markup=markup)

    # @bot.message_handler(content_types=['text'])
    # def send_text(message):
    #     if message.text.lower() == 't':
    #         try:
    #             bot.send_message(message.chat.id, f"temp: {get_data()[0]}\n"
    #                                               f"condition: {get_data()[1]}\n"
    #                                               f"temp_max: {get_data()[3]}\n"
    #                                               f"temp_min: {get_data()[2]}\n")
    #         except Exception as ex:
    #             print(ex)
    #             bot.send_message(message.chat.id, "Disconnection!!!")
    #
    #     elif message.text == "d":
    #         a = telebot.types.ReplyKeyboardRemove()
    #         bot.send_message(message.from_user.id, 'Delete', reply_markup=a)
    #
    #     else:
    #         bot.send_message(message.chat.id, "Wrong command")


    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)  # или просто print(e) если у вас логгера нет
            time.sleep(15)


# if __name__ == "__main__":
telegram_bot(token)
    # get_data()



# def new_orders():
#     new_orders_list = []
#     driver.find_element(By.CLASS_NAME, "ButtonStyles__Container-sc-1kch7k2-0.ePYDqV").click()
#     # order_window = driver.find_element(By.ID, "inbox_scrollable_container_id")
#
#     # new_orders_text = driver.find_element(By.CLASS_NAME, "ModalStyles__Container-sc-5v78xr-1 dIOCaP").find_elements(By.CLASS_NAME, "NotificationStyles__Description-sc-1iolh49-4")
#     new_orders_text = driver.find_element(By.CLASS_NAME, "ModalStyles__Container-sc-5v78xr-1 dIOCaP").text
#     new_orders_list.append(new_orders_text)
#
#     # for n in range(len(new_orders)):
#     #     order_info = new_orders[n].text
#     #     print(order_info)
#     #     new_orders_list.append(order_info)
#
#     return new_orders_list

# from get_info import *
# import telebot
# from auth_data import token
#
#
# def telegram_bot(token):
#     bot = telebot.TeleBot(token)
#
#     @bot.message_handler(commands=['start'])
#     def start_message(message):
#         bot.send_message(message.chat.id, "Работаем")
#         # Functions to open webpages for search
#         enter_web_page()
#
#     @bot.message_handler(content_types=['text'])
#     def send_text(message):
#
#         if message.text.lower() == 'n':
#             bot.send_message(message.chat.id, "Открываем окно сообщений")
#             click_note()
#
#         elif message.text.lower() == 't':
#             bot.send_message(message.chat.id, "Ищем новые сообщения")
#             inbox_text = inbox_orders()
#             for i in range(len(inbox_text)):
#                 bot.send_message(message.chat.id, f"{inbox_text[i]}")
#                 print(inbox_text[i])
#
#         elif message.text.lower() != 'o':
#             bot.send_message(message.chat.id, "Код принят")
#             enter_code(message.text)
#             enter_chat()
#
#         elif message.text.lower() == 'o':
#             try:
#
#                 # OPEN ORDERS Section
#                 open_temp = open_orders()
#
#                 if open_temp == []:
#                     bot.send_message(message.chat.id, "-- Нет ордеров: -- ОТКРЫТЫЕ --")
#                     print("-- Нет ордеров: -- ОТКРЫТЫЕ --")
#                 else:
#                     for n in range(len(open_temp)):
#
#                         # Text for search in Youtube
#                         search_open = open_temp[n]['марка:'] + " " + open_temp[n]['проблема:']
#                         search_open = search_open.split('.')[0]
#
#                         # Taking all text about an order in one message
#                         open_temp_2 = list(open_temp[n].items())
#                         open_temp_3 = ''
#                         for item in open_temp_2:
#                             tpl = " ".join(item)
#                             open_temp_3 = open_temp_3 + tpl + '\n'
#
#                         # Printing info about order in one message
#                         bot.send_message(message.chat.id, f"{open_temp_3}")
#                         print(open_temp_3)
#
#                         # Text for searching in youtube
#                         bot.send_message(message.chat.id, f"{search_open}")
#                         print(search_open)
#
#
#                 # WORKING ORDERS Section
#                 working_temp = working_orders()
#
#                 if working_temp == []:
#                     bot.send_message(message.chat.id, "-- Нет ордеров: -- В РАБОТЕ --")
#                     print("-- Нет ордеров: -- В РАБОТЕ --")
#                 else:
#                     for n in range(len(working_temp)):
#                         # Text for search in Youtube
#                         search_working = working_temp[n]['марка:'] + " " + working_temp[n]['проблема:']
#                         search_working = search_working.split('.')[0]
#
#                         # Taking all text about an order in one message
#                         working_temp_2 = list(working_temp[n].items())
#                         working_temp_3 = ''
#                         for item in working_temp_2:
#                             tpl = " ".join(item)
#                             working_temp_3 = working_temp_3 + tpl + '\n'
#
#                         # Printing info about order in one message
#                         bot.send_message(message.chat.id, f"{working_temp_3}")
#                         print(working_temp_3)
#
#                         # Text for searching in youtube
#                         bot.send_message(message.chat.id, f"{search_working}")
#                         print(search_working)
#
#
#             except Exception as ex:
#                 print(ex)
#                 bot.send_message(message.chat.id, "Error!")
#         else:
#             bot.send_message(message.chat.id, "I like myself!")
#     while True:
#         try:
#             bot.polling(none_stop=True)
#         except Exception as e:
#             print(e)
#             time.sleep(60)
#
#
# if __name__ == "__main__":
#     telegram_bot(token=token)


# @bot.message_handler(commands=['loop'])
# def loop_message(message):
#     while True:
#         if message.text == "loop":
#             try:
#                 bot.send_message(message.chat.id, "Открываем окно ...")
#                 click_open()
#                 time.sleep(3)
#                 bot.send_message(message.chat.id, "Список заказов в окне:")
#                 all_list = check_all()
#                 if all_list == []:
#                     bot.send_message(message.chat.id, "Заказов нет")
#                 else:
#                     for item in all_list:
#                         bot.send_message(message.chat.id, f"{item}")
#                         print(item)
#                 time.sleep(57)
#             except Exception as ex:
#                 print(ex)
#                 bot.send_message(message.chat.id, "Error in loop!")
#         elif message.text == "stop":
#             bot.send_message(message.chat.id, "... Ожидаем указа ... ")
#             pass

# @bot.message_handler(commands=['stop'])
# def loop_message(message):
#     while True:
#         try:
#             bot.send_message(message.chat.id, "... Ожидаем указа ... ")
#             time.sleep(60000)
#         except Exception as ex:
#             print(ex)
#             bot.send_message(message.chat.id, "Error in stop!")