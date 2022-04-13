from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.Time, nullable=False)
    no_of_people = db.Column(db.Integer, nullable=False)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method=="POST":
        name = request.form.get("name")
        email = request.form.get("email")
        of_date = request.form.get("date")
        of_time = request.form.get("time")
        people = request.form.get("people")
        

    return render_template("book.html")

if __name__ == "__main__":
    app.run(debug=True)