import telebot
import requests
from unicodedata import category

TOKEN = "7324019305:AAFUurcmiE-xdebBNWDE5WSvOsp2eyzuLek"
daun_bot  = telebot.TeleBot(TOKEN)
COMMAND_LIST = ["/get_locations_names", "/get_positive_reviews_by_name", "/get_negative_reviews_by_name", "/get_avg_visits_by_name", "/get_metrics_by_name"]
URL = "https://yupest2.pythonanywhere.com/"
GET_METRICS = "api/celestial/get_stats_by_id/?id="
GET_LOCATIONS = "api/celestial/get_locations/"
GET_REVIEWS = "api/celestial/get_reviews_by_id/?id="  # вместо id указать идентификатор места
GET_STATS = "api/celestial/get_stats_by_id/?id="
GET_AVG_VISITS = "api/celestial/get_average_visits_by_id/?id="
response_locations = requests.get(URL + GET_LOCATIONS, verify=False)
responseplacesJSON = response_locations.json()
locations_list = responseplacesJSON["locations"]


@daun_bot.message_handler(commands=["start"])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_help = telebot.types.KeyboardButton("/help")
    markup.add(btn_help)
    daun_bot.send_message(message.from_user.id, "Привет. Я - чат-бот с информацией о городе Поднебесный. Чтобы подробнее узнать, что я умею, воспользуйся командой /help", reply_markup=markup)

@daun_bot.message_handler(commands=["help"])
def help(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("/get_negative_reviews_by_name")
    btn2 = telebot.types.KeyboardButton("/get_avg_visits_by_name")
    btn3 = telebot.types.KeyboardButton("/get_metrics_by_name")
    btn4 = telebot.types.KeyboardButton("/recommend_location")
    btn5 = telebot.types.KeyboardButton("/get_positive_reviews_by_name")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    daun_bot.send_message(message.from_user.id, '''
    /get_positive_reviews_by_name + название локации - получить позитивные отзывы о локации, имя которой вы указали
/get_negative_reviews_by_name + название локации - получить негативные отзывы о локации, имя которой вы указали
/get_avg_visits_by_name + название локации - получить среднюю посещаемость локации, имя которой вы указали
/get_metrics_by_name + название локации - получить количество лайков и средний рейтинг локации, имя которой вы указали
/recommend_location - порекомендовать локацию
    ''', reply_markup=markup)


@daun_bot.message_handler(commands=["recommend_location"])
def recommend_location(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("образование")
    btn2 = telebot.types.KeyboardButton("исторические памятники")
    btn3 = telebot.types.KeyboardButton("парки")
    btn4 = telebot.types.KeyboardButton("спорт")
    btn5 = telebot.types.KeyboardButton("пляжи")
    btn6 = telebot.types.KeyboardButton("музеи")
    btn7 = telebot.types.KeyboardButton("театры")
    btn8 = telebot.types.KeyboardButton("развлечение")
    btn9 = telebot.types.KeyboardButton("фонтаны")
    btn10 = telebot.types.KeyboardButton("средство размещения")
    btn11 = telebot.types.KeyboardButton("зоопарки")
    btn12 = telebot.types.KeyboardButton("торговые центры")
    btn13 = telebot.types.KeyboardButton("кафе")
    btn14 = telebot.types.KeyboardButton("аквариумы")
    btn15 = telebot.types.KeyboardButton("сады")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)
    markup.add(btn5)
    markup.add(btn6)
    markup.add(btn7)
    markup.add(btn8)
    markup.add(btn9)
    markup.add(btn10)
    markup.add(btn11)
    markup.add(btn12)
    markup.add(btn13)
    markup.add(btn14)
    markup.add(btn15)
    daun_bot.send_message(message.from_user.id, "Выберите категорию локации, которую вы бы хотели посетить", reply_markup=markup)


@daun_bot.message_handler(content_types=["text"])
def get_text_msg(message):
    print('message')
    res = []
    print(message.text)
    for i in locations_list:
        print(message.text)
        if i["category"].lower() == message.text:
            res.append(i["name"] + "\n" + "\n" + i["description"])
    daun_bot.send_message(message.from_user.id,"\n".join(res))


# def get_locations_names():
#     names = [i["name"] for i in locations_list]
#     return sorted(names)
#
#
# def get_positive_reviews_by_name(spec_url2, msg):
#     loc_name = (msg.text)[30:]
#     loc_id = ""
#     for i in locations_list:
#         if i["name"] == loc_name:
#             loc_id = i["id"]
#     response_reviews = requests.get(URL + spec_url2 + loc_id)
#     response_reviewsJSON = response_reviews.json()
#     pos_reviews = [i["review"] for i in response_reviewsJSON if i["rating"] >= 4]
#     return "\n".join(pos_reviews)
#
# def get_negative_reviews_by_name(spec_url2, msg):
#     loc_name = (msg.text)[30:]
#     loc_id = ""
#     for i in locations_list:
#         if i["name"] == loc_name:
#             loc_id = i["id"]
#     response_reviews = requests.get(URL + spec_url2 + loc_id)
#     response_reviewsJSON = response_reviews.json()
#     pos_reviews = [i["review"] for i in response_reviewsJSON if i["rating"] < 4]
#     return "\n".join(pos_reviews)
#
#
# def get_avg_visits_by_name(spec_url3, msg):
#     loc_name = (msg.text)[24:]
#     loc_id = ""
#     for i in locations_list:
#         if i["name"] == loc_name:
#             loc_id = i["id"]
#     response_avg_visits = requests.get(URL + spec_url3 + loc_id)
#     response_avg_visitsJSON = response_avg_visits.json()
#     result = f'Средняя посещаемость локации "{loc_name}" составляет {response_avg_visitsJSON["avg_visits"]} '
#     return result
#
#
# def get_metrics_by_name(spec_url4, msg):
#     loc_name = (msg.text)[21:]
#     loc_id = ""
#     for i in locations_list:
#         if i["name"] == loc_name:
#             loc_id = i["id"]
#     response_metrics = requests.get(URL + spec_url4 + loc_id)
#     response_metricsJSON = response_metrics.json()
#     res = f'''
#     Количество лайков локации "{loc_name}" составляет: {response_metricsJSON["likes"]}
#     Средний рейтинг локации "{loc_name}" составляет: {sum(response_metricsJSON["ratings"]) / len(response_metricsJSON["ratings"])}
#     '''
#     return res


# def recommend_location(msg):
#     res = "Вам подойдут следующие локации:"
#     if "!" in msg:
#         if "есть" in msg or "пить" in msg.lower():
#             for i in locations_list:
#                 if i["category"] == "торговые центры" or i["category"] == "кафе":
#                     res += "\n"
#                     res += "\n"
#                     res += i["name"]
#                     res += "\n"
#                     res += "\n"
#                     res += i["description"]
#         elif "развле" in msg.lower():
#             for i in locations_list:
#                 if i["category"] == "развлечение":
#                     res += "\n"
#                     res += "\n"
#                     res += i["name"]
#                     res += "\n"
#                     res += "\n"
#                     res += i["description"]
#         elif "отель" in msg.lower() or "гостиница" in msg.lower() or "жить" in msg.lower() or "разме" in msg.lower():
#             for i in locations_list:
#                 if i["category"] == "средство размещения":
#                     res += "\n"
#                     res += "\n"
#                     res += i["name"]
#                     res += "\n"
#                     res += "\n"
#                     res += i["description"]
#         elif "спорт" in msg.lower():
#             for i in locations_list:
#                 if i["category"] == "спорт":
#                     res += "\n"
#                     res += "\n"
#                     res += i["name"]
#                     res += "\n"
#                     res += "\n"
#                     res += i["description"]
#         elif "отдых" in msg.lower() or "досуг" in msg.lower():
#             for i in locations_list:
#                 if i["category"] in ["исторические памятники", "парки", "пляжи", "музеи", "театры", "фонтаны", "зоопарки", "аквариумы", "сады"]:
#                     res += "\n"
#                     res += "\n"
#                     res += i["name"]
#                     res += "\n"
#                     res += "\n"
#                     res += i["description"]
#         elif "уч" in msg.lower() or "образов" in msg.lower():
#             for i in locations_list:
#                 if i["category"] == "образование":
#                     res += "\n"
#                     res += "\n"
#                     res += i["name"]
#                     res += "\n"
#                     res += "\n"
#                     res += i["description"]
#     return res




# @daun_bot.message_handler(content_types=["text"])
# def get_text_msg(message):
#     if message.text.lower() in ["привет", "/start"]:
#         daun_bot.send_message(message.from_user.id, "Привет. Я - чат-бот с информацией о городе Поднебесный. Чтобы подробнее узнать, что я умею, воспользуйся командой /help")
#     elif message.text == "/get_locations_names":
#         daun_bot.send_message(message.from_user.id, "\n".join(get_locations_names()))
#     elif "/get_positive_reviews_by_name" in message.text:
#         daun_bot.send_message(message.from_user.id, get_positive_reviews_by_name(GET_REVIEWS, message))
#     elif "/get_negative_reviews_by_name" in message.text:
#         daun_bot.send_message(message.from_user.id, get_negative_reviews_by_name(GET_REVIEWS, message))
#     elif "/get_avg_visits_by_name" in message.text:
#         daun_bot.send_message(message.from_user.id, get_avg_visits_by_name(GET_AVG_VISITS, message))
#     elif "/get_metrics_by_name" in message.text:
#         daun_bot.send_message(message.from_user.id, get_metrics_by_name(GET_METRICS, message))
#     elif message.text.lower() in ["/help", "помощь", "помогите"]:
#         daun_bot.send_message(message.from_user.id, '''
#         Вот что я умею:
#         /get_locations_names - получить список локаций города Поднебесный
#         /get_positive_reviews_by_name + название локации - получить позитивные отзывы о локации, имя которой вы указали
#         /get_negative_reviews_by_name + название локации - получить негативные отзывы о локации, имя которой вы указали
#         /get_avg_visits_by_name + название локации - получить среднюю посещаемость локации, имя которой вы указали
#         /get_metrics_by_name + название локации - получить количество лайков и средний рейтинг локации, имя которой вы указали
#         ''')
#     elif "!" in message.text:
#         daun_bot.send_message(message.from_user.id, recommend_location(message.text))

daun_bot.polling(none_stop=True, interval=0)




