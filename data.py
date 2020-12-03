import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Table config
class Game(db.Model):
    __tablename__ = "matches"
    id = db.Column(db.Integer, primary_key=True)
    game_date = db.Column(db.DateTime, nullable=False)
    game_mode = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String)
    champ = db.Column(db.String, nullable=False)
    k = db.Column(db.Integer, nullable=False)
    d = db.Column(db.Integer, nullable=False)
    a = db.Column(db.Integer, nullable=False)
    cs = db.Column(db.Integer, nullable=False)
    dmg = db.Column(db.Integer, nullable=False)
    shield = db.Column(db.Integer, nullable=False)
    heal = db.Column(db.Integer, nullable=False)
    gold = db.Column(db.Integer, nullable=False)
    vision = db.Column(db.String)
    result = db.Column(db.String)
    score = db.Column(db.Integer, nullable=False)
    rchamp = db.Column(db.String)
    rk = db.Column(db.String)
    rd = db.Column(db.String)
    ra = db.Column(db.String)
    rcs = db.Column(db.String)
    rgold = db.Column(db.String)

# Champion pool
champs = [
"Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion Sol", "Azir",
"Bard", "Blitzcrank", "Brand", "Braum",
"Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki",
"Darius", "Diana", "Dr. Mundo", "Draven",
"Ekko", "Elise", "Evelynn", "Ezreal",
"Fiddlesticks", "Fiora", "Fizz",
"Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves",
"Hecarim", "Heimerdinger",
"Illaoi", "Irelia", "Ivern",
"Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx",
"Kai'Sa", "Kalista", "Karma", "Karthus", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled", "Kog'Maw",
"LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux",
"Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune", "Mordekaiser", "Morgana",
"Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nocturne", "Nunu & Willump",
"Olaf", "Orianna", "Ornn",
"Pantheon", "Poppy", "Pyke",
"Qiyana", "Quinn",
"Rakan", "Rammus", "Rek'Sai", "Renekton", "Rengar", "Riven", "Rumble", "Ryze",
"Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra",
"Tahm Kench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch",
"Udyr", "Urgot",
"Varus", "Vayne", "Veigar", "Vel'Koz", "Vi", "Viktor", "Vladimir", "Volibear",
"Warwick", "Wukong",
"Xayah", "Xerath", "Xin Zhao",
"Yasuo", "Yone", "Yorick", "Yuumi",
"Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra"
]