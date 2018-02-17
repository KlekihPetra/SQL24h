#!/usr/bin/python

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

    
# start the server
app.run(debug=True)
