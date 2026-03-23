from flask import Flask, render_template, redirect
from ia.class_neurone import Neurone
from colors import generate_color, to_rgb, from_rgb

neurone = Neurone()

def init():
    return Flask(__name__)

def index():
    color = generate_color()
    is_red = neurone.is_red(color)
    color = to_rgb(color)
    return render_template("index.html",couleur=color,is_red=is_red,neurone=neurone.etat)

def update(couleur,is_red):
    couleur = from_rgb(eval(couleur))
    is_red = 1 if is_red == "True" else 0
    neurone.update(couleur,is_red)
    return redirect("/")

