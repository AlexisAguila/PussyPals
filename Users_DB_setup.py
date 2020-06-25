import sqlite3

class Users():

    def __init__(self):
        Connection = sqlite3.connect('User.db')
        Connection = Connection.cursor()
        Connection.execute('CREATE TABLE USERS (Username TEXT NOT NULL UNIQUE, Firstname TEXT NOT NULL, Lastname TEXT NOT NULL, Age INTEGER, Catname TEXT, Password TEXT))')
        Connection.close()

    def insert_user(self,Username,Firstname,Lastname,Age,Catname,Password):
        connection = sqlite3.connect('Users.db')
        cursor = connection.cursor()
        Insert_querie = """INSERT INTO USERS (Username,Firstname,Lastname,Age,Catname,Password) VALUES (?,?,?,?,?,?);"""
        User_tuple = (Username,Firstname,Lastname,Age,Catname,Password)
        temp = cursor.execute(Insert_querie, User_tuple)
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