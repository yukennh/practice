import sqlite3
conn = sqlite3.connect("notebook.db")
cursor = conn.cursor()

cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='notes'")
schema = cursor.fetchone()
print(schema[0])

date = str(input("Date: "))
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