import sqlite3 as sql
import time
import os

'''

This module serve a DataBase connection

In each method i make same thing:
	conn = sql.connect(table_name)
	cursor = conn.cursor()
	It is nessecary!
	Because if i don't do it. The module 'sqlite3' throws exceptions. As object cursor was created in another thread.
	I can't controll theads, because it is inner threads of module telebot

All of this methods get rid me of sql for database

'''

table_name = "data.db"

def insert(title, course):
	conn = sql.connect(table_name)
	cursor = conn.cursor()
	cursor.execute('''INSERT INTO courses VALUES ('{}', '{}')'''.format(title, course))
	conn.commit()

def insert_all(d):
	for key in d:
		insert(key, d[key])
	ready()

def select(where=''):
	conn = sql.connect(table_name)
	cursor = conn.cursor()
	cursor.execute('select * from courses '+where)
	return cursor.fetchall()

def trade_from_db(currency1, currency2, value):
	currencys = select()
	if currencys == []:
		return trade(currency1, currency2, value)
	scale1 = float(select("where title='{}'".format(currency1.upper()))[0][1])
	scale2 = float(select("where title='{}'".format(currency2.upper()))[0][1])
	return value/scale1*scale2

def clear_table():
	conn = sql.connect(table_name)
	cursor = conn.cursor()
	cursor.execute('''delete from courses where 1=1''')
	conn.commit()

def create_table(cursor, conn):
	cursor.execute('''CREATE TABLE courses (title text, course text)''')
	conn.commit()


def ready():
	f = open('time.txt', 'w')
	f.write(str(time.time()))
	f.close()

def is_overtime():
	f = open('time.txt', 'r')
	old_time = float(f.read().strip())
	f.close()
	return time.time() - old_time > 10 * 60



