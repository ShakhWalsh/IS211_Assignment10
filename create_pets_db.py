import sqlite3

conn = sqlite3.connect("pets.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
""")

cursor.execute("""
CREATE TABLE pet (
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
)
""")

cursor.execute("""
CREATE TABLE person_pet (
    person_id INTEGER,
    pet_id INTEGER
)
""")

conn.commit()
conn.close()
print("pets.db created with schema!")
