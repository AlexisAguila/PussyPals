import sqlite3

class Users():

    def __init__(self):
        Connection = sqlite3.connect('catDaddy.db')
        Connection = Connection.cursor()
        # Connection.execute('CREATE TABLE Profiles (Name VARCHAR(12) UNIQUE, Pin INT, Sleep FLOAT, Purr FLOAT,WetFood FLOAT, DryFood FLOAT, Butt FLOAT, Face FLOAT, Body FLOAT, Humans FLOAT, Catnip FLOAT, Outside FLOAT)')
        Connection.close()

    # not sure if the *args is going to work right, maybe try to just use parameters at first
    def insert_user(self, *args):
        connection = sqlite3.connect('catDaddy.db')
        cursor = connection.cursor()
        Insert_querie = """INSERT INTO Profiles (Name, Pin, Sleep, Purr, WetFood, DryFood, Butt, Face, Body, Humans, Catnip, Outside) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);"""

        cursor.execute("INSERT INTO Profiles (Name, Pin, Sleep, Purr, WetFood, DryFood, Butt, Face, Body, Humans, Catnip, Outside) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                       (args[0], args[1], args[2],args[3],args[4],args[5],args[6],args[7],args[8],args[9],args[10],args[11],))
        # User_tuple = (Username,Firstname,Lastname,Age,Catname,Password)
        # cur.execute("INSERT INTO Profiles (Name, Pin, Sleep, Purr, WetFood, DryFood, Butt, Face, Body, Humans, Catnip, Outside) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(nm, pn, sl, pr, wf, df, bt, fa, bo, hu, cn, ou))
        connection.commit()
        cursor.close()

    def retrieve_user(self,Username):
        connection=sqlite3.connect('Users.db')
        cursor=connection.cursor()
        Get_user="""SELECT * FROM USERS WHERE Username = ?;"""
        cursor.execute(Get_user,(Username,))
        rows=cursor.fetchone()
        cursor.close()
        return rows
        #TODO return render_template(htmlfile, rows=rows)