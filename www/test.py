#!/usr/bin/python

import mySQL

c, con = mySQL.OpenConnection()
n_tables = mySQL.Tables(c,con)

print(n_tables)

mySQL.CloseConnection(con)
