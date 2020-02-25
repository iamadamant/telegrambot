import urllib.request as request
import json
import datetime

'''

This module parse data for bot.
'''

source_url = 'https://api.exchangeratesapi.io/latest?base={}'
historical_url = 'https://api.exchangeratesapi.io/history?start_at={}&end_at={}&base={}&symbols={}'

def get_list(base='usd'):
	'''

	Its returns list of currencies(валюты[надеюсь :)]) 
	'''
	res = {}
	req = request.urlopen(source_url.format(base.upper()))
	data = req.read()
	json_data = json.loads(data)
	for key in json_data['rates']:
		res.update({key: round(float(json_data['rates'][key]), 2)})
	return res



def get_history(base, target, days_count):
	'''
	
	This method useful for visualize. Its provides a nessecary data for him:
		days- It is list of date
		values - It is list of currency scale
	'''
	base = base.upper()
	target = target.upper()
	days = []
	values = []
	end = str(datetime.datetime.today()).split()[0]
	start = str(datetime.datetime.today()-datetime.timedelta(days=days_count)).split()[0]
	res = {}
	req = request.urlopen(historical_url.format(start, end, base, target))
	data = req.read()
	json_data = json.loads(data)
	for key in json_data['rates']:
		days.append(key)
		values.append(round(float(json_data['rates'][key][target]), 2))
	values.sort()
	return days, values

