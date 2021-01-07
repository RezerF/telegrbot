import telebot
import requests

bot = telebot.TeleBot('')

req_data_usd = requests.get('https://api.binance.com/api/v1/trades?symbol=BTCUSDT&limit=1')
req_data_rub = requests.get('https://api.binance.com/api/v1/trades?symbol=BTCRUB&limit=1')
data_usd = req_data_usd.json()
data_rub = req_data_rub.json()
bitcoin_price = float(data_usd[0]['price'])
bitcoin_price_rub = float(data_rub[0]['price'])
count = 0
@bot.message_handler(content_types=['text'])
def start_price(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, f"Bitcoin price is ${bitcoin_price}\n"
                                               f"or {bitcoin_price_rub} RUB"
                                               f" Input count coins to calculate sum\n"
                                               f"For example: 2.4 or 3")
        bot.register_next_step_handler(message, get_count) #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'July push the /start')

def get_count(message):
    global count
    count = float(message.text)
    bot.send_message(message.from_user.id, f'Sum of {count} Bitcoin  is ${bitcoin_price*count}\n'
                                           f'or {bitcoin_price_rub*count} RUB')

# def get_age(message):
#     global age
#     while age == 0: #проверяем что возраст изменился
#         try:
#              age = int(message.text) #проверяем, что возраст введен корректн
#         except Exception:
#              bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
#       # bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "Howdy, how are you doing?")
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


bot.polling(none_stop=True, interval=0.5)
