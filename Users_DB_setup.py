import sqlite3
import numpy as np


class Users():

    def __init__(self):
        Connection = sqlite3.connect('catDaddy.db')
        Connection = Connection.cursor()
        #Connection.execute('CREATE TABLE Profiles (Name VARCHAR(12) UNIQUE, Pin INT, Sleep FLOAT, Purr FLOAT,WetFood FLOAT, DryFood FLOAT, Butt FLOAT, Face FLOAT, Body FLOAT, Humans FLOAT, Catnip FLOAT, Outside FLOAT)')
        Connection.close()


    def insert_user(self, *args):
        connection = sqlite3.connect('catDaddy.db')
        cursor = connection.cursor()
        # Insert_querie = """INSERT INTO Profiles (Name, Pin, Sleep, Purr, WetFood, DryFood, Butt, Face, Body, Humans, Catnip, Outside) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);"""
        cursor.execute("INSERT INTO Profiles (Name, Pin, Sleep, Purr, WetFood, DryFood, Butt, Face, Body, Humans, Catnip, Outside) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                       (args[0], args[1], args[2],args[3],args[4],args[5],args[6],args[7],args[8],args[9],args[10],args[11]))
        connection.commit()
        cursor.close()

    def get_user_name(self, *args):
        connection = sqlite3.connect('catDaddy.db')
        cursor = connection.cursor()
        cursor.execute("select * from Profiles where Name=? AND Pin=?", (args[0], args[1]))
        cat = np.array(cursor.fetchall())
        return cat[0][0]



    def match_maker(self, *args):

        connection = sqlite3.connect('catDaddy.db')
        cursor = connection.cursor()
        # To_Match = cursor.execute("select * from Profiles where Name=? AND Pin=?", (args[0], args[1])) # arg[0] = name, arg[1] = pin of selected cat to match-make
        cursor.execute("select * from Profiles where Name=?", (args[0],)) # returns an array of all users except the one being match-made
        name = np.array(cursor.fetchall())

        cursor.execute("select * from Profiles where Name!=?", (args[0],)) # returns an array of all users except the one being match-made
        cat = np.array(cursor.fetchall())

        matche_names = []
        match_values = []

        for i in range(0,len(cat)):
            matche_names.append(cat[i][0])
            match_values.append(0)
            for c in range (2,11):

                if name[0][c] == cat[i][c]:
                    match_values[i] = match_values[i] + 1

        magicIndex = 0
        tempHighest = 0
        count = 0
        for x in match_values:
            if x > tempHighest:
                tempHighest = x
                magicIndex = count
            count += 1

        return matche_names[magicIndex]  # Returns the user with the most attributes that match eachother, else if there is no match, returns the user at the top of the table
