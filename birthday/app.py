from flask import Flask, request, render_template 
#'Flask' creates the web app
#'request' reads the data from the form
#'render_template' loads the HTML file from the templates/ folder
#type 'pip install -r requirements.txt' to install flask as it is already indicated in the text the requirements needed
import sqlite3

app = Flask(__name__) #this is a standard naming convention needed for flask which tells flask where to find resources

@app.route("/", methods=["GET", "POST"]) #this defines the action that will be done. If this is not set, it's default action is GET.
def index(): #this is the name of the function
    if request.method == "POST": #request method is define in the html
        first_name = request.form.get("first_name") #name indicated in the html tag
        last_name = request.form.get("last_name") #name indicated in the html tag
        year = request.form.get("year") #name indicated in the html tag
        month = request.form.get("month") #name indicated in the html tag
        day = request.form.get("day") #name indicated in the html tag

        birthday = f"{year.zfill(4)}/{month.zfill(2)}/{day.zfill(2)}" #this set's the variable into a printable format. 'zfill(n)' makes sure the number of character to be indicated.

        conn = sqlite3.connect("birthday.db") #to connect to the database
        c = conn.cursor() #to set a cursor that will do the action SQL query
        c.execute("INSERT INTO names (first_name, last_name, birthday) VALUES (?, ?, ?)",(first_name, last_name, birthday)) #the SQL query that will run to enter the data from the form to the database.
        # the (?,?,?) is a placeholder that it will use for the SQL query, it is define after the whole SQL query but still within the cursor execution.
        conn.commit() #to save the output done by the SQL query
        conn.close() #to close the data base

        return f"Added {first_name} {last_name} with birthday {birthday}!" #shows the name and the birthday added

    # This now loads templates/index.html
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)