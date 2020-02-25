import telebot
from parserc import *
from db import *
from trade import *
import re
from visualizer import *

'''

It is main module. It creates the bot. Such it handle commands, which user provides
'''


bot = telebot.TeleBot('871816127:AAHXkmbjaVSaoQeKOBeAX4dhoLJ11g7kOnM')


@bot.message_handler(commands=['list'])
def execute_command(message): 
	mess = []
	if is_overtime():
		curencies_d = get_list()
		clear_table()
		insert_all(curencies_d)
		for key in curencies_d:
			mess.append(str(key)+': '+str(curencies_d.get(key)))
	else:
		curencies = select()
		for currecy in curencies:
			mess.append(str(currecy[0])+': '+str(currecy[1]))

	for line in mess:
		bot.send_message(message.chat.id, line)	

@bot.message_handler(commands=['start'])
def say_hello(message):
	bot.send_message(message.chat.id, 'hello')
		

@bot.message_handler(commands=['обменять'])
def test(message):
	currencies = re.findall('[A-Z]+', message.text)
	value = float(re.findall('[0-9]+', message.text)[0])
	answ = trade_from_db(currencies[0], currencies[1], value)
	bot.send_message(message.chat.id, round(float(answ), 2))

@bot.message_handler(commands=['history'])
def test(message):
	currencies = re.findall('[A-Z]+', message.text)
	count_days = float(re.findall('[0-9]+', message.text)[0])
	days, values = get_history(currencies[0], currencies[1], count_days)
	photo = get_plot(days, values)
	bot.send_photo(message.chat.id, open(photo, 'rb'))

bot.polling()
