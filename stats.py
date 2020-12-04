from flask import Flask, jsonify, render_template, request
from data import *
from sqlalchemy import and_, or_

def stats():
    return render_template("stats.html", champs=champs)

def query():
    filters = request.get_json("filters")
    if filters['mode'] and filters['champ']:
        data = (Game.query
                .filter_by(game_mode=filters['mode'])
                .filter_by(champ=filters['champ'])
                .order_by(Game.id.desc())
                .limit(int(filters['gameNumber']))
                .all()
                )
    elif filters['mode'] or filters['champ']:
        data = (Game.query
         .filter(or_(Game.game_mode.ilike(filters['mode']), Game.champ.ilike(filters['champ'])))
         .order_by(Game.id.desc())
         .limit(int(filters['gameNumber']))
         .all()
         )
    else:
        data = Game.query.order_by(Game.id.desc()).limit(int(filters['gameNumber'])).all()
    return jsonify({"status": "success"})