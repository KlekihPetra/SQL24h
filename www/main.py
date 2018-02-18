#!/usr/bin/python

from flask import Flask, render_template
import mySQL

app = Flask(__name__)

@app.route('/')
def index():
	# Get the number of lists in the db
	c, con = mySQL.OpenConnection()
	tables = mySQL.Tables(c,con)
	return render_template('index.html', n_tables=len(tables), tables=tables)

    
# start the server
app.run(debug=True)
