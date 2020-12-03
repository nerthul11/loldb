from flask import Flask, render_template, request
from data import *

def stats():
    return render_template("stats.html", champs=champs)