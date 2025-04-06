# query_pets.py
# This script queries the pets.db for a person's pets

import sqlite3

def get_person_and_pets(person_id):
    conn = sqlite3.connect("pets.db")
    cursor = conn.cursor()

    cursor.execute("SELECT first_name, last_name, age FROM person WHERE id=?", (person_id,))
    person = cursor.fetchone()

    if not person:
        return None, None

    cursor.execute('''
        SELECT pet.name, pet.breed, pet.age, pet.dead
        FROM pet
        JOIN person_pet ON pet.id = person_pet.pet_id
        WHERE person_pet.person_id=?
    ''', (person_id,))
    pets = cursor.fetchall()

    conn.close()
    return person, pets

while True:
    user_input = input("Enter person ID (-1 to exit): ")
    if user_input == "-1":
        break

    try:
        person_id = int(user_input)
    except ValueError:
        print("Please enter a valid number.")
        continue

    person, pets = get_person_and_pets(person_id)

    if not person:
        print("No person found with that ID.")
        continue

    first_name, last_name, age = person
    print(f"{first_name} {last_name}, {age} years old")

    for name, breed, pet_age, dead in pets:
        status = "who is" if not dead else "who was"
        print(f"  Owned {name}, a {breed}, {status} {pet_age} years old.")
