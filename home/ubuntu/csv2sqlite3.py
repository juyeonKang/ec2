#!/usr/bin/python3

import sqlite3

flat = open('flat.csv').read()

List = flat.split('\n')[:-1];

column = [x+" text, " for x in List[0].split(',')]
column = ''.join(column)
sql = "CREATE TABLE flat (" + column[:-2] + ")"

conn = sqlite3.connect('flat.db')
c = conn.cursor()
c.execute(sql)  

for item in List[1:len(List)] : 
	c.execute('INSERT INTO flat VALUES (?,?,?,?,?,?,?,?,?)', tuple(item.split(',')))

conn.commit()
