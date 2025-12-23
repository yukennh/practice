import sqlite3
conn = sqlite3.connect("notebook.db")
cursor = conn.cursor()

cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='notes'")
schema = cursor.fetchone()
print(schema[0])

day = int(input("What is the day today? "))
while day < 1 or day > 31:
    print("Enter a valid day from 1-31.")
    day = int(input("What is the day today? "))

month = int(input("What is the month today? "))
while month < 1 or month > 12:
    print("Enter a valid month from 1-12.")
    month = int(input("What is the month today? "))

date = str(f"{day}/{month}/2025")
note = str(input("Enter your notes here: "))
while note == "":
    print("Your notes cannot be blank.")
    note = str(input("Enter your notes here: "))

#instead of using (f"INSERT INTO notes (date, notes) VALUES ('{date}','{note}');") as an SQL, the one below is used to avoid sql inject
cursor.execute("INSERT INTO notes (date, notes) VALUES (?,?)",(date, note))
conn.commit()

print(f"\n Your entry is saved! \n")

cursor.execute("SELECT * FROM notes")
entries = cursor.fetchall()

for entry in entries:
    print(entry)

conn.close()