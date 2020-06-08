# This file runs the application
from flask import Flask, render_template, request
import sqlite3 as sql
import datetime
app = Flask(__name__, template_folder='./')

# Home page
@app.route('/')
def home():
    return render_template('Front_Page.html')

# int main()
if __name__ == '__main__':
    app.run(debug = True)
