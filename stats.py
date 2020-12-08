from flask import Flask, jsonify, render_template, request
from data import *
from sqlalchemy import and_, or_

def stats():
    return render_template("stats.html", champs=champs)

def query():
    filters = request.get_json("filters")
    if filters['mode'] and filters['champ']:
        games = (Game.query
                .filter_by(game_mode=filters['mode'])
                .filter_by(champ=filters['champ'])
                .order_by(Game.id.desc())
                .limit(int(filters['gameNumber']))
                .all()
                )
    elif filters['mode'] or filters['champ']:
        games = (Game.query
         .filter(or_(Game.game_mode.ilike(filters['mode']), Game.champ.ilike(filters['champ'])))
         .order_by(Game.id.desc())
         .limit(int(filters['gameNumber']))
         .all()
         )
    else:
        games = Game.query.order_by(Game.id.desc()).limit(int(filters['gameNumber'])).all()

    if games:
        # Defining and resetting variables
        games_played = len(games)
        game_modes = {"normal": 0, "ranked": 0, "flex": 0, "aram": 0}
        wins = 0
        ka = 0
        d = 0
        cs = 0
        gold = 0
        duration = 0

        for match in games:
            mode = match.game_mode
            game_modes[mode] += 1
            if match.result == "W":
                wins += 1
            ka += match.k + match.a
            d += match.d
            cs += match.cs
            gold += match.gold
            duration += match.duration

        kda = round(ka / d, 2)
        winrate = round(wins * 100 / games_played, 2)
        csm = round(cs * 60 / duration, 2)
        gpm = round(gold * 60 / duration, 2)
        avg_duration = int(duration / games_played)
        avg_duration = f"{avg_duration // 60:02}:{avg_duration % 60:02}"
        data = {
            "gameModes": game_modes,
            "gamesPlayed": games_played,
            "winrate": winrate,
            "kda": kda,
            "csm": csm,
            "gpm": gpm,
            "averageDuration": avg_duration
        }

        print(data)
        return jsonify(data)
    else:
        return jsonify({"error": "No games found"})