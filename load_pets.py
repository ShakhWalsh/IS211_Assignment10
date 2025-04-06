# load_pets.py
# This script inserts initial data into the pets.db database

import sqlite3

conn = sqlite3.connect("pets.db")
cursor = conn.cursor()

# Insert people
people = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
]
cursor.executemany("INSERT INTO person VALUES (?, ?, ?, ?)", people)

# Insert pets
pets = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]
cursor.executemany("INSERT INTO pet VALUES (?, ?, ?, ?, ?)", pets)

# Insert relationships
relationships = [
    (1, 1), (1, 2),
    (2, 3), (2, 4),
    (3, 5),
    (4, 6)
]
cursor.executemany("INSERT INTO person_pet VALUES (?, ?)", relationships)

conn.commit()
conn.close()
