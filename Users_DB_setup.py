import sqlite3
import numpy as np


class Users():

    def __init__(self):
        Connection = sqlite3.connect('catDaddy.db')
        Connection = Connection.cursor()
        # Connection.execute('CREATE TABLE Profiles (Name VARCHAR(12) UNIQUE, Pin INT, Sleep FLOAT, Purr FLOAT,WetFood FLOAT, DryFood FLOAT, Butt FLOAT, Face FLOAT, Body FLOAT, Humans FLOAT, Catnip FLOAT, Outside FLOAT)')
        Connection.close()


    def insert_user(self, *args):
        connection = sqlite3.connect('catDaddy.db')
        cursor = connection.cursor()
        # Insert_querie = """INSERT INTO Profiles (Name, Pin, Sleep, Purr, WetFood, DryFood, Butt, Face, Body, Humans, Catnip, Outside) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);"""
        cursor.execute("INSERT INTO Profiles (Name, Pin, Sleep, Purr, WetFood, DryFood, Butt, Face, Body, Humans, Catnip, Outside) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                       (args[0], args[1], args[2],args[3],args[4],args[5],args[6],args[7],args[8],args[9],args[10],args[11]))
        connection.commit()
        cursor.close()

    # I THINK WE CAN DELETE THIS FUNCTION, ALEXIS WHEN U READ THIS U DECIDE *********************************************************************************
    def retrieve_user(self,Username):
        connection=sqlite3.connect('Users.db')
        cursor=connection.cursor()
        Get_user="""SELECT * FROM USERS WHERE Username = ?;"""
        cursor.execute(Get_user,(Username,))
        rows=cursor.fetchone()
        cursor.close()
        return rows
        #TODO return render_template(htmlfile, rows=rows)


    def get_user_name(self, *args):
        connection = sqlite3.connect('catDaddy.db')
        cursor = connection.cursor()
        cursor.execute("select * from Profiles where Name=? AND Pin=?", (args[0], args[1]))
        cat = np.array(cursor.fetchall())

        return cat[0][0]

    def match_maker(self, *args):
        # going to implement a way to show percentage of match with all the other users in the database, try to add a way give the 'best match'
        # maybe try to just create a way to give the 'best match' first
        connection = sqlite3.connect('catDaddy.db')
        cursor = connection.cursor()
        # To_Match = cursor.execute("select * from Profiles where Name=? AND Pin=?", (args[0], args[1])) # arg[0] = name, arg[1] = pin of selected cat to match-make
        cat = np.array(cursor.fetchall())
        # cursor.execute("select NAME from Profiles where Name!=? AND (select)", (cat[0][0],))  # cat[0][0] is name of cat

        # p = cursor.execute("select *, ((case when Sleep IS ? THEN 1 WHEN Sleep IS NULL THEN 0 Else NULL END "
        #                "+ CASE WHEN Purr is ? THEN 1 WHEN Purr IS NULL THEN 0 ELSE NULL END"
        #                "+ CASE WHEN WetFood IS ? THEN 1 WHEN WetFood IS NULL THEN 0 ELSE NULL END) AS Matches"
        #                ") "
        #                "FROM Profiles WHERE Matches IS NOT NULL "
        #                "ORDER BY Matches DESC "
        #                "LIMIT 1", (To_Match,))

        cursor.execute("SELECT Name FROM Profiles WHERE Sleep=(Select Sleep From Profiles where Name=? AND Pin=?)", (args[0], args[1]))
        cat = np.array(cursor.fetchall())

        return cat[1][0]


