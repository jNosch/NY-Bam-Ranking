from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'leaderboard.db')}"
db = SQLAlchemy(app)


#Database

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    time_seconds = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()




@app.route("/")
def index():
    return render_template("index.html")

@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html")



@app.route("/api/submit", methods=["POST"])
def submit():
    data = request.json
    name = data.get("name")
    time_seconds = data.get("time_seconds")

    if not name or time_seconds is None:
        return jsonify({"error": "Missing name or time"}), 400

    record = Record(name=name, time_seconds=time_seconds)
    db.session.add(record)
    db.session.commit()
    return jsonify({"success": True})


@app.route("/api/leaderboard")
def get_leadeboard():
    mode = request.args.get("mode","all")

    query = Record.query
    if mode == "today":
        today = datetime.utcnow().date()
        query = query.filter(db.func.date(Record.timestamp) == today)

    records = query.order_by(Record.time_seconds.asc()).all()

    result = [{"name": r.name, "time_seconds": r.time_seconds, "timestamp": r.timestamp.isoformat()} for r in records]
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
