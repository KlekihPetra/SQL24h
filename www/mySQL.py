#!/usr/bin/python

import MySQLdb as db


# Get the number of tables
def Tables(c, con):
	command = 'SHOW TABLES;'
	c.execute(command)
	res = c.fetchall()
	tables = [el[0] for el in res]
	return tables

def OpenConnection():
	con = db.connect(host='localhost', user='root', passwd='yukka31', db='CANARYAIRLINES')
	c = con.cursor()
	return c, con

def CloseConnection(con):
	con.close()
	return 0