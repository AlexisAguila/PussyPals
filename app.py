# This file runs the application
from flask import Flask, render_template, request
import sqlite3 as sql
import datetime
app = Flask(__name__, template_folder='./')

# Home page
@app.route('/')
def home():
    return render_template('Front_Page.html')

# About_Page
@app.route('/About_Page')
def about():
    return render_template('About_Page.html')

# About_Page
@app.route('/Match_Maker')
def match_maker():
    return render_template('Match_Maker.html')

# Page to create profile
@app.route('/createProf')
def create_prof():
    return render_template('createProf.html')

# What happens after someone clicks  sumbit on createProf.html
@app.route('/addprof', methods = ['POST', 'GET'])
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
                cur.execute("INSERT INTO Profiles (Name, Pin, Sleep, Purr, WetFood, DryFood, Butt, Face, Body, Humans, Catnip, Outside) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (nm,pn,sl,pr,wf,df,bt,fa,bo,hu,cn,ou))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "Error in insert operation"
        finally:
            con.close()
            return render_template("Match_Maker.html")

# What happens after some prowls on Match_Maker.html
@app.route('/showProfiles', methods = ['POST', 'GET'])
def showprofiles():
    #rs = request.form['Restaurant']

    con = sql.connect("catDaddy.db")
    con.row_factory = sql.Row

    cur = con.cursor()
#    cur.execute("select * from Reviews where Restaurant=?", (rs,))
    cur.execute("select * from Profiles")

    rows = cur.fetchall();
#    return render_template("showReviews.html", rows=rows, msg=rs)
    return render_template("showProfiles.html", rows=rows)



# int main()
if __name__ == '__main__':
    app.run(debug = True)
