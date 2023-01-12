from flask import Flask;
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config.DesarrolloConfig')
db = SQLAlchemy(app)

from anime.views import base
app.register_blueprint(base)


from anime.anime2.views import anime2
app.register_blueprint(anime2)

with app.app_context(): 
    db.create_all()