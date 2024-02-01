import telebot
import webbrowser
import config

# https://www.youtube.com/watch?v=sjq8KSMWxQ4
bot = telebot.TeleBot('6761816132:AAGJi7uRjJqICOF-vi1s4pgDpIrJkqcc0Uw')

@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://www.immowelt.de/suche/hamburg/wohnungen/mieten?sort=relevanz')

@bot.message_handler(commands=['start','main'])
def notification(message):
    bot.send_message(message.chat.id, f'Привет! {message.from_user.first_name},{message.from_user.last_name}')

@bot.message_handler(commands=['help'])
def notification(message):
    bot.send_message(message.chat.id, '<b>Hue</b> <em><u>Help!</u></em>', parse_mode='html')

@bot.message_handler(commands=['info'])
def notification1(message):
    bot.send_message(message.chat.id,
        f"""Квартира!=> <b>{config.my_object.title}</b>
Опалення!=><b>{config.my_object.heizkosten}</b>
Аренда!=><b>{config.my_object.kaltmiete}</b>
Дод.витратри!=><b>{config.my_object.nebencosten}</b>
Локація!=><b>{config.my_object.location}</b>""", parse_mode='html')

def test():
    bot.reply_to(message, f'ID: {message.from_user.id}')
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
      bot.send_message(message.chat.id, f'Привет! {message.from_user.first_name},{message.from_user.last_name}')
    elif(message.text.lower() == 'id'):
        bot.reply_to(message, f'ID: {message.from_user.id}')

bot.polling(none_stop=True)



