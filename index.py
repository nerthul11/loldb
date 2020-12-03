import datetime

from flask import Flask, render_template, request
from data import *

def index():
    if request.method == "POST":
        data = Game(
            game_date=datetime.datetime.today(),
            game_mode=request.form.get("type"),
            duration=int(request.form.get("minutes")) * 60 + int(request.form.get("seconds")),
            role=request.form.get("role"),
            champ=request.form.get("champ"),
            k=request.form.get("kills"),
            d=request.form.get("deaths"),
            a=request.form.get("assists"),
            cs=request.form.get("cs"),
            dmg=request.form.get("dmg"),
            shield=request.form.get("shield"),
            heal=request.form.get("heal"),
            gold=request.form.get("gold"),
            vision=request.form.get("vision"),
            result=request.form.get("result"),
            score=request.form.get("score"),
            rchamp=request.form.get("rchamp"),
            rk=request.form.get("rkills"),
            rd=request.form.get("rdeaths"),
            ra=request.form.get("rassists"),
            rcs=request.form.get("rcs"),
            rgold=request.form.get("rgold")
        )
        db.session.add(data)
        db.session.commit()
    return render_template("input.html", champs=champs)