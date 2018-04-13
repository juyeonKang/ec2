#!/usr/bin/python3

import sqlite3
from bottle import route, run, template, request, post

@route('/')
def main():
	#return '<b> Hello:D<br> this page is my first page! </b>'
	f = open('8080html','r')
	multiline = f.read()
	return multiline


@route('/db', method='POST')
def db():
	conn = sqlite3.connect('flat.db')
	c = conn.cursor()
	str1 = "SELECT DISTINCT "
	str2 = " FROM books JOIN Rtable ON ISBN = b_ISBN JOIN authors ON AuID = a_AuID JOIN publishers ON b_PubID = p_PubID"
	
	input_str = request.POST.getall('column')
	column = ['< '+x[2:]+' >' for x in input_str]
	column = [tuple(column)]
	input_str = [x+' text,' for x in input_str]
	input_str = ''.join(input_str)[:-1]

	fstring = str1 + input_str + str2

	c.execute(fstring)
	result=c.fetchall()
	result = column + result
	c.close()
	output = template('make_table', rows=result)

	return str(output)

run(reloader = True, host='0.0.0.0', port=8080)

