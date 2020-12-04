import datetime
import os

from data import *
from flask import Flask

from index import index
from stats import query, stats

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('POSTGRES')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

app.add_url_rule('/', view_func=index, methods=["GET","POST"])
app.add_url_rule('/stats', view_func=stats)
app.add_url_rule('/query', view_func=query, methods=["POST"])