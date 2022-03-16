from crypt import methods
from re import X
from flask import Flask, redirect, url_for, render_template, request
from helper import multiple_cool,run_model,voice_definer, define_which_sound
import multiprocessing
from playsound import playsound
import time


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
        global user_choice
        user_choice = 'rap'
        seed_input = request.form.get("seed")
        size = int(request.form.get("size"))
        global button_choice
        button_choice = request.form.get("clicked_btn1")
        global x
        x = run_model('rap',button_choice,seed_input,size)

        return render_template("rap.html", result = x)
    else:
        return render_template("rap.html")


@app.route("/poems",methods=["POST","GET"])
def poems():
    if request.method == "POST":
        global user_choice
        user_choice = 'poems'
        seed_input = request.form.get("seed")
        size = int(request.form.get("size"))
        global button_choice
        button_choice = request.form.get("clicked_btn2")
        global x
        x = run_model('poems',button_choice,seed_input,size)

        return render_template("poems.html", result = x)
    else:
        return render_template("poems.html")


@app.route("/politic-speech",methods=["POST","GET"])
def politic():
    if request.method == "POST":
        global user_choice
        user_choice = 'politic-speech'
        seed_input = request.form.get("seed")
        size = int(request.form.get("size"))
        global button_choice
        button_choice = request.form.get("clicked_btn3")
        global x
        x = run_model('politic-speech',button_choice,seed_input,size)
        return render_template("politic-speech.html", result = x)
    else:
        return render_template("politic-speech.html")

@app.route("/sound")
def sound():
    """multiple actions at the same time
    background sound and speech to text """
    multiple_cool(user_choice, button_choice, x)
    return (''), 204

if __name__ == "__main__":
    app.run(port=7000,debug=True)