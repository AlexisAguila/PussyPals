import sqlite3

class Message_Posts():

    def __init__(self):
        Connection = sqlite3.connect('discussion_messages.db')
        Connection = Connection.cursor()
        #Connection.execute('CREATE TABLE Messages (Name VARCHAR(12) , Message TEXT)')
        Connection.close()

    def insert_message(self, Name, message):
        connection = sqlite3.connect('discussion_messages.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Messages (Name,Message) VALUES (?,?)",
                       (Name,message))
        connection.commit()
        cursor.close()