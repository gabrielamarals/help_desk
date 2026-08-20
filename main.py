from database.database import create_ticket_table, create_user_table


def initialize_database():
    create_user_table()
    create_ticket_table()


if __name__ == "__main__":
    initialize_database()
    print("Help Desk database initialized successfully.")
