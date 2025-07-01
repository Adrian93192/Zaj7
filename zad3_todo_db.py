from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db = SQLAlchemy(app)

# Model zadania
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

@app.route("/", methods=["GET", "POST"])
def tasks():
    if request.method == "POST":
        task_text = request.form["task"]
        new_task = Task(text=task_text)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("tasks"))
    all_tasks = Task.query.all()
    return render_template("todo.html", tasks=all_tasks)

@app.route("/done/<int:id>")
def mark_done(id):
    task = Task.query.get_or_404(id)
    task.done = True
    db.session.commit()
    return redirect(url_for("tasks"))

@app.route("/delete/<int:id>")
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("tasks"))

if __name__ == "__main__":
    app.run(debug=True)
