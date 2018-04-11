#!/usr/bin/python3

import sqlite3
from bottle import route, run, template, request

@route('/')
def main():
	#return '<b> Hello:D<br> this page is my first page! </b>'
	multiline =  """<meta charset="utf-8">

	<form action="http://52.78.114.3:8080/db">
		<input type="checkbox" name="ISBN" value="b_ISBN"> ISBN <br>
		<input type="checkbox" name="Title" value="b_Title"> Title <br>
		<input type="checkbox" name="Author" value="a_AuName"> Author<br>
		<input type="checkbox" name="Publisher" value="p_PubName"> Publisher<br>
		<input type="checkbox" name="Price" value="b_Price"> Price <br>
		<input type="submit" value="전송">
	</form>
	"""
	return multiline


@route('/db')
def db():
	conn = sqlite3.connect('flat.db')
	c = conn.cursor()
	str1 = "SELECT DISTINCT "
	str2 = " FROM books JOIN Rtable ON ISBN = b_ISBN JOIN authors ON AuID = a_AuID JOIN publishers ON b_PubID = p_PubID"
	
	select = ''

	ISBN = request.GET.ISBN
	Title = request.GET.Title
	Author = request.GET.Author
	Publisher = request.GET.Publisher
	Price = request.GET.Price
	
	if ISBN:
		select += ISBN+', '
	if Title:
		select += Title+', '
	if Author:
		select += Author+', '
	if Publisher:
		select += Publisher+', '
	if Price:
		select += Price+', '

	fstring = str1 + select[:-2] + str2

	c.execute(fstring)
	result=c.fetchall()
	c.close()
	output = template('make_table', rows=result)

	return str(output)

run(reloader = True, host='0.0.0.0', port=8080)
