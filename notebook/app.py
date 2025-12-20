import sqlite3
conn = sqlite3.connect("notebook.db")
cursor = conn.cursor()

date = "20/12/2025"
note = "This is a sample entry from VSCODE through python without the use of HTML"

#instead of using (f"INSERT INTO notes (date, notes) VALUES ('{date}','{note}');") as an SQL, the one below is used to avoid sql inject
cursor.execute("INSERT INTO notes (date, notes) VALUES (?,?)",(date, note))
conn.commit()

conn.close()