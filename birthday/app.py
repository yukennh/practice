from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# HTML template inline for simplicity
HTML_FORM = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Birthday List</title>
</head>
<body>
    <form action="/" method="post">
        <input type="text" name="first_name" placeholder="First Name"/>
        <input type="text" name="last_name" placeholder="Last Name"/>
        <input type="number" name="month" placeholder="Month"/>
        <input type="number" name="day" placeholder="Day"/>
        <input type="submit" value="Add Birthday"/>
    </form>
</body>
</html>
"""

def init_db():
    conn = sqlite3.connect("birthdays.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS names (
                    id INTEGER PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT,
                    birthday TEXT
                )""")
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        month = request.form.get("month")
        day = request.form.get("day")

        # Format birthday as MM-DD
        birthday = f"{month.zfill(2)}-{day.zfill(2)}"

        conn = sqlite3.connect("birthdays.db")
        c = conn.cursor()
        c.execute("INSERT INTO names (first_name, last_name, birthday) VALUES (?, ?, ?)",
                  (first_name, last_name, birthday))
        conn.commit()
        conn.close()

        return f"Added {first_name} {last_name} with birthday {birthday}!"

    return render_template_string(HTML_FORM)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
