from flask import Flask, request, url_for, render_template

app = Flask(__name__)

@app.route("/player", methods=["POST"])
def player():
  audios = request.form["bibcodes"]
  audio_list = audios.split(',')
  style = url_for("static", filename="styles.css")
  script = url_for("static", filename="player.js")
  return render_template("player.html", audios=audio_list, style=style, script=script)