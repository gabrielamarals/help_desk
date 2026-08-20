import sqlite3

def create_user_table():
    connection = sqlite3.connect("helpdesk.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE, 
    role TEXT NOT NULL,
    password_hash TEXT NOT NULL)
""")
    connection.commit()
    cursor.close()
    connection.close()

def create_ticket_table():
    connection = sqlite3.connect("helpdesk.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL, 
    description TEXT NOT NULL,
    priority TEXT NOT NULL,
    status TEXT NOT NULL,
    created_by INTEGER NOT NULL)

    FOREIGN KEY (created_by)
                REFERENCES users(id)
""")    
    connection.commit()
    cursor.close()
    connection.close()

