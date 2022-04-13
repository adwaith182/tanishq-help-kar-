from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, time

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///userDB.db"
app.config["SECRET_KEY"] = "ABCD"
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
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
        of_date = datetime.strptime(request.form.get("date"), "%Y-%m-%d")
        of_time = datetime.strptime(request.form.get("time"), "%H:%M").time()
        people = request.form.get("people")
        new_user = User(name=name, email=email, date=of_date, time=of_time, no_of_people=people)
        db.session.add(new_user)
        db.session.commit()
        flash("User Registered Successfully!")
        
    return render_template("book.html")
