from flask import Flask, jsonify, render_template, request
from data import *

def stats():
    return render_template("stats.html", champs=champs)

def query():
    # Do the thing according to filters
    filters = request.get_json("filters")
    gameNumber = int(filters["gameNumber"])
    filters.pop("gameNumber")
    games = Game.query
    pop = []
    for filter in filters:
        if not filters[filter]:
            pop.append(filter)
    for filter in pop:
        filters.pop(filter)
    games = games.filter_by(**filters)
    games = games.order_by(Game.id.desc()).limit(gameNumber).all()
    if games:
        # Defining and resetting variables
        games_played = len(games)
        game_modes = {"normal": 0, "ranked": 0, "flex": 0, "aram": 0}
        roles = {"top": 0, "jg": 0, "mid": 0, "adc": 0, "sup": 0}
        wins = 0
        ka = 0
        d = 0
        cs = 0
        gold = 0
        vision = 0
        duration = 0

        # Iterate through games to create results
        for match in games:
            mode = match.game_mode
            role = match.role
            game_modes[mode] += 1
            if role != "":
                roles[role] += 1
            if match.result == "W":
                wins += 1
            ka += match.k + match.a
            d += match.d
            cs += match.cs
            gold += match.gold
            duration += match.duration
            if match.vision != "":
                vision += int(match.vision)

        # Work with the results
        kda = round(ka / d, 2)
        winrate = round(wins * 100 / games_played, 2)
        csm = round(cs * 60 / duration, 2)
        gpm = round(gold * 60 / duration, 2)
        vision = round(vision * 3600 / duration, 2)
        avg_duration = int(duration / games_played)
        avg_duration = f"{avg_duration // 60:02}:{avg_duration % 60:02}"

        # Compose the JSON to return
        data = {
            "success": True,
            "gameModes": game_modes,
            "roles": roles,
            "gamesPlayed": games_played,
            "winrate": winrate,
            "kda": kda,
            "csm": csm,
            "gpm": gpm,
            "vision": vision,
            "averageDuration": avg_duration
        }
        return jsonify(data)
    else:
        return jsonify({"success": False})