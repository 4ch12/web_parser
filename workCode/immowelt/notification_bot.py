import telebot



# https://www.youtube.com/watch?v=sjq8KSMWxQ4
bot = telebot.TeleBot('')
chat_id = 294706978
def notification(city,gesammite,links_flat,heizkosten_value,nebencosten):
# , gesammite, links_flat,
#  nebenkosten, heizkosten_valu):
 bot.send_message(chat_id,
f"""Посилання!=> <b>{links_flat}</b>
Nebenkosten+Kalmite=> <b>{gesammite}</b>
Опалення!=><b>{heizkosten_value}</b>
Локація!=><b>{city}</b>
Дод. витрати!=><b>{nebencosten}</b>""",  parse_mode='html')
        #            print("City:", )
        # print("Gesammite:", self.gesammite)
        # print("Links Flat:", self.links_flat)
        # print("Nebenkosten:", self.nebencosten)
        # print("Heizkosten Value:", self.heizkosten_value)

# @bot.message_handler(commands=['site'])
# def site(message):
#  bot.reply_to(message, f'ID: {message.from_user.id}')
# #     webbrowser.open('https://www.immowelt.de/suche/hamburg/wohnungen/mieten?sort=relevanz')

# @bot.message_handler(commands=['start','main'])
# def notification(message):
#     bot.send_message(message.chat.id, f'Привет! {message.from_user.first_name},{message.from_user.last_name}')

# @bot.message_handler(commands=['help'])
# def notification(message):
#     bot.send_message(message.chat.id, '<b>Hue</b> <em><u>Help!</u></em>', parse_mode='html')

# @bot.message_handler(commands=['info'])
# def notification1(message):
#     bot.send_message(message.chat.id,'TEST', parse_mode='html')
#         f"""Квартира!=> <b>{config.my_object.title}</b>
# Опалення!=><b>{config.my_object.heizkosten}</b>
# Аренда!=><b>{config.my_object.kaltmiete}</b>
# Дод.витратри!=><b>{config.my_object.nebencosten}</b>
# Локація!=><b>{config.my_object.location}</b>"""

    # bot.reply_to(message, f'ID: {message.from_user.id}')
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'привет':
#       bot.send_message(message.chat.id, f'Привет! {message.from_user.first_name},{message.from_user.last_name}')
#     elif(message.text.lower() == 'id'):
#         bot.reply_to(message, f'ID: {message.from_user.id}')

bot.polling(none_stop=True)



