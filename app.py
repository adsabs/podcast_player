from flask import Flask, request, url_for, render_template
import json

app = Flask(__name__)

def create_app(**config):
  return app

@app.route("/player", methods=["POST"])
def player():
  audios = json.loads(request.form["sources"])
  audio_list = [] # in the format [[title, source], ...]
  for title, source in audios.items():
    audio_list.append([title, source])
  style = url_for("static", filename="styles.css")
  script = url_for("static", filename="player.js")
  return render_template("player.html", audios=audio_list, style=style, script=script)