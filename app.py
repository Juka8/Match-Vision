
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

players = []

@app.route("/")
def index():
    return render_template("index.html", players=players)

@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    goals = int(request.form.get("goals", 0))
    assists = int(request.form.get("assists", 0))
    presence = request.form.get("presence", "no")

    for p in players:
        if p["name"].lower() == name.lower():
            p["goals"] += goals
            p["assists"] += assists
            p["presence"] = presence
            break
    else:
        players.append({
            "name": name,
            "goals": goals,
            "assists": assists,
            "presence": presence
        })

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
