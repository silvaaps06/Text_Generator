from crypt import methods
from flask import Flask, redirect, url_for, render_template, request
from helper import multiple_cool,run_model,voice_definer, define_which_sound


app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/rap",methods=["POST","GET"])
def rap():
    if request.method == "POST":
        seed_input = request.form.get("seed")
        size = int(request.form.get("size"))
        button_choice = request.form.get("clicked_btn1")
        result = multiple_cool('rap',button_choice,run_model('rap',button_choice,seed_input,size))
        return render_template("rap.html", result = result[2])
    else:
        return render_template("rap.html")


@app.route("/poems")
def poems():
    if request.method == "POST":
        seed_input = request.form.get("seed")
        size = int(request.form.get("size"))
        button_choice = request.form.get("clicked_btn1")
        result = multiple_cool('poems',button_choice,run_model('poems',button_choice,seed_input,size))
        return render_template("poems.html", result = result[2])
    else:
        return render_template("poems.html")


@app.route("/politic-speech")
def politic():
    if request.method == "POST":
        seed_input = request.form.get("seed")
        size = int(request.form.get("size"))
        button_choice = request.form.get("clicked_btn1")
        result = multiple_cool('politic-speech',button_choice,run_model('politic-speech',button_choice,seed_input,size))
        return render_template("politic-speech.html", result = result[2])
    else:
        return render_template("politic-speech.html")


if __name__ == "__main__":
    app.run(debug=True)