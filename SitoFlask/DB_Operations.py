import sqlite3
import datetime
def get_compiti():
    connection = sqlite3.connect("compiti.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS "compiti" (
	"id"	INTEGER,
	"descrizione"	TEXT,
	"titolo"	TEXT,
    "materia"    TEXT,
	"data_scadenza"	DATETIME,
	"creation_date"	DATETIME,
	"update_date"	DATETIME default current_timestamp,
	PRIMARY KEY("id" AUTOINCREMENT)
);""")
    cursor.execute("""SELECT id, descrizione, titolo, data_scadenza FROM COMPITI;""")
    rows = cursor.fetchall()
    return rows


#inserting data to db
def add_text(title, description, data_scadenza, materia):
    #database connection
    # print("text_value = " +text_value)
    connection = sqlite3.connect("compiti.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS "compiti" (
	"id"	INTEGER,
	"descrizione"	TEXT,
	"titolo"	TEXT,
    "materia"    TEXT,
	"data_scadenza"	DATETIME,
	"creation_date"	DATETIME,
	"update_date"	DATETIME default current_timestamp,
	PRIMARY KEY("id" AUTOINCREMENT)
);""")
    cursor.execute("""INSERT INTO compiti(titolo, descrizione, data_scadenza, materia, creation_date) 
                   VALUES (?,?,?,?,?)"""
                   , (title, description, data_scadenza, materia, datetime.datetime.now()))
    connection.commit()
    return 1