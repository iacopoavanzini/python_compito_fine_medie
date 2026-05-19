import sqlite3


#inserting data to db
def add_text(title, description):
    #database connection
    # print("text_value = " +text_value)
    connection = sqlite3.connect("compiti.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS compiti (id	INTEGER,descrizione	TEXT,titolo	TEXT,PRIMARY KEY(id AUTOINCREMENT));")
    cursor.execute("INSERT INTO compiti(titolo, descrizione) VALUES (?,?)", (title, description))
    connection.commit()
    return 1