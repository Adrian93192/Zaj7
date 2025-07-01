from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///teachers.db"
db = SQLAlchemy(app)

# Model nauczyciela
class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(50), nullable=False)

@app.route("/")
def index():
    teachers = Teacher.query.all()
    return render_template("teachers.html", teachers=teachers)

@app.route("/add", methods=["GET", "POST"])
def add_teacher():
    if request.method == "POST":
        name = request.form["name"]
        subject = request.form["subject"]
        time = request.form["time"]
        new_teacher = Teacher(name=name, subject=subject, time=time)
        db.session.add(new_teacher)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_teacher.html")

@app.route("/delete/<int:id>")
def delete_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    db.session.delete(teacher)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
