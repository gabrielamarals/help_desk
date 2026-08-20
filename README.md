# Help Desk

A small help desk system I am building to practice backend development, relational databases and API design with Python.

> **Work in progress:** the project currently contains the initial SQLite database layer. The REST API and ticket workflows are still being implemented.

## Current scope

- user table with unique email and roles;
- ticket table linked to its creator through a foreign key;
- SQLite database initialization;
- database constraints for required fields.

## Planned next steps

- FastAPI REST endpoints;
- ticket creation and status updates;
- user authentication;
- input validation;
- automated tests;
- API documentation.

## Technologies

Python · SQLite · SQL

## Run locally

```bash
python main.py
```

This initializes the local `helpdesk.db` database.

## What I am learning

This project is focused on practicing relational modeling, foreign keys, database constraints and the structure of a backend application before adding the API layer.
