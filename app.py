# This file runs the application
from flask import Flask, render_template, request
import sqlite3 as sql
import datetime
import numpy as np
from Users_DB_setup import Users
from Discussion_DB_setup import Message_Posts

app = Flask(__name__, template_folder='./')
user_messages=Message_Posts()
user = Users()  # creates user object from class Users


# Home page
@app.route('/')
def home():
    return render_template('Front_Page.html')


# About_Page
@app.route('/About_Page')
def about():
    return render_template('About_Page.html')


# Discussion
@app.route('/Discussion', methods=['POST', 'GET'])
def discussion():
    #user_messages.insert_message("Hello","World1")  #TODO add a text box
    con = sql.connect("discussion_messages.db")

    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from Messages")
    rows=cur.fetchall()

    if request.method == 'POST':
        nm = request.form['Name']
        msg = request.form['Message']

        user_messages.insert_message(nm,msg)  #TODO add a text box



    return render_template('Discussion.html',rows=rows)


# FAQ
@app.route('/FAQ')
def faq():
    return render_template('FAQ.html')


# Match_Maker gives them the option to create a profile or search
@app.route('/Match_Maker')
def match_maker():
    return render_template('Match_Maker.html')


# Page to create profile
@app.route('/createProf')
def create_prof():
    return render_template('createProf.html')


# Page to search for matches
@app.route('/catSearch')
def cat_search():
    return render_template('catSearch.html')

def checkForMissing(temp):
    if (len(temp) == 0):
        return True
    else:
        return False

# What happens after someone clicks  sumbit on createProf.html
@app.route('/addprof', methods=['POST', 'GET'])
def addprof():
    if request.method == 'POST':
        try:
            nm = request.form['Name']
            pn = request.form['Pin']
            sl = request.form['Sleep']
            pr = request.form['Purr']
            wf = request.form['WetFood']
            df = request.form['DryFood']
            bt = request.form['Butt']
            fa = request.form['Face']
            bo = request.form['Body']
            hu = request.form['Humans']
            cn = request.form['Catnip']
            ou = request.form['Outside']

            with sql.connect("catDaddy.db") as con:
                cur = con.cursor()

                msg = ""

                if (checkForMissing(nm) == True):
                    msg = "Error in insert operation"
                elif (checkForMissing(pn) == True):
                    msg = "Error in insert operation"
                elif (checkForMissing(sl) == True):
                    msg = "Error in insert operation"
                elif (checkForMissing(pr) == True):
                    msg = "Error in insert operation"
                elif (checkForMissing(wf) == True):
                    msg = "Error in insert operation"
                elif (checkForMissing(df) == True):
                    msg = "Error in insert operation"
                elif (checkForMissing(bt) == True):
                    msg = "Error in insert operation"
                elif (checkForMissing(fa) == True):
                    msg = "Error in insert operation"
                elif (checkForMissing(bo) == True):
                    msg = "Error in insert operation"
                elif (checkForMissing(hu) == True):
                    msg = "Error in insert operation"
                elif (checkForMissing(cn) == True):
                    msg = "Error in insert operation"
                elif (checkForMissing(ou) == True):
                    msg = "Error in insert operation"
                else:
                    msg = "Record successfully added"
                # can delete this, leaving it just in case its needed again
                # cur.execute("INSERT INTO Profiles (Name, Pin, Sleep, Purr, WetFood, DryFood, Butt, Face, Body, Humans, Catnip, Outside) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (nm,pn,sl,pr,wf,df,bt,fa,bo,hu,cn,ou))
                user.insert_user(nm, pn, sl, pr, wf, df, bt, fa, bo, hu, cn, ou)
                con.commit()
                # msg = "Record successfully added"
        except:
            con.rollback()
            msg = "Error in insert operation"
        finally:
            con.close()
            if (msg == "Record successfully added"):
                return render_template("Match_Maker.html")
            else:
                return render_template("createProf.html")


# What happens after some prowls on Match_Maker.html
@app.route('/showProfiles', methods=['POST', 'GET'])
def showProfiles():
    nm = request.form['Name']
    pn = request.form['Pin']

    con = sql.connect("catDaddy.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from Profiles where Name=? AND Pin=?", (nm, pn))
    cat = np.array(cur.fetchall())
    if (len(cat) == 0):
        return render_template("Match_Maker.html")
    Cat = user.get_user_name(nm, pn)  # Cat gets the name using the function in class

    cur.execute("select * from Profiles where Name!=?", (cat[0][0],))
    rows = cur.fetchall()  # tried passing 'rows' from function in class also, however never populated graph with data, so just doing it here instead
    match = user.match_maker(nm, pn)

    return render_template("showProfiles.html", rows=rows, msg=Cat, m=match)


# int main()
if __name__ == '__main__':
    app.run(debug=True)
