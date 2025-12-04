from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        year = request.form.get("year")
        month = request.form.get("month")
        day = request.form.get("day")

        birthday = f"{year.zfill(4)}/{month.zfill(2)}/{day.zfill(2)}"

        conn = sqlite3.connect("birthday.db")
        c = conn.cursor()
        c.execute("INSERT INTO names (first_name, last_name, birthday) VALUES (?, ?, ?)",
                  (first_name, last_name, birthday))
        conn.commit()
        conn.close()

        return f"Added {first_name} {last_name} with birthday {birthday}!"

    # This now loads templates/index.html
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)