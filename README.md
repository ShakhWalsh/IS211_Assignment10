# IS211_Assignment10

This repository contains the Week 10 assignment for IS211, covering relational databases and SQLite usage.

## Contents

- `music.sql` – SQL schema for a simple music database (artists, albums, songs)
- `create_pets_db.py` – Creates the SQLite database and tables for the pet example
- `load_pets.py` – Loads person, pet, and relationship data into the database
- `query_pets.py` – CLI tool to query pets owned by a person by ID

## How to Use

1. Run `create_pets_db.py` to create the `pets.db` file
2. Run `load_pets.py` to populate the database
3. Run `query_pets.py` and enter a person ID to see their pets
4. Enter `-1` to exit the query program
