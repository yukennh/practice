import sqlite3
conn = sqlite3.connect("notebook.db")
cursor = conn.cursor()

cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='notes'")
schema = cursor.fetchone()
print(schema[0])

date = "21/12/2025"
note = "This is a sample entry from VSCODE through python without the use of HTML to show that my entry is added to the notes. 2"

#instead of using (f"INSERT INTO notes (date, notes) VALUES ('{date}','{note}');") as an SQL, the one below is used to avoid sql inject
cursor.execute("INSERT INTO notes (date, notes) VALUES (?,?)",(date, note))
conn.commit()

print(f"\n Your entry is saved! \n")

cursor.execute("SELECT * FROM notes")
entries = cursor.fetchall()

for entry in entries:
    print(entry)

conn.close()