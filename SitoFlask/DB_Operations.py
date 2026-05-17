import sqlite3


#inserting data to db
def add_text(text_value):
    #database connection
    print("text_value = " +text_value)
    connection = sqlite3.connect("compiti.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS compiti (id	INTEGER,descrizione	TEXT,titolo	TEXT,PRIMARY KEY(id AUTOINCREMENT));")
    cursor.execute("INSERT INTO compiti(titolo) VALUES (?)", (text_value,))
    connection.commit()
    return 1