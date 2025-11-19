from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        return f"Received: {name} - {month}/{day}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
