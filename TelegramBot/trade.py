import parserc
from db import *

'''

This module i made decision didn't use. But i thought its can be useful, so i left that
'''

def trade(currency1, currency2, value):
	lst = parserc.get_list(currency1)
	scale = float(lst.get(currency2.upper()))
	return value*scale



