from app.database import (
    create_ticket,
    create_ticket_table,
    create_user,
    create_user_table,
)

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return{"message" : "help Desk API funcionando"}