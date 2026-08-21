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
    created_by INTEGER NOT NULL,
    FOREIGN KEY (created_by)
        REFERENCES users(id)
    )
    """)
    connection.commit()
    cursor.close()
    connection.close()


def create_user(nome, email, role, password_hash):
    connection = sqlite3.connect("helpdesk.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users(
        nome,
        email,
        role,
        password_hash
        ) VALUES (?, ?, ?, ?)
    """, (nome, email, role, password_hash))
    user_id = cursor.lastrowid

    connection.commit()
    cursor.close()
    connection.close()
    return user_id


def create_ticket(title, description, priority, status, created_by):
    connection = sqlite3.connect("helpdesk.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tickets(
        title,
        description,
        priority,
        status,
        created_by
        ) VALUES (?, ?, ?, ?, ?)
    """, (title, description, priority, status, created_by))
    ticket_id = cursor.lastrowid

    connection.commit()
    cursor.close()
    connection.close()
    return ticket_id

