from flask import render_template, Blueprint, request,redirect,url_for
from anime.models import Animes

from anime import db

base = Blueprint('base',__name__)

@base.route("/")
@base.route("/Home")
def home():
    return render_template("home.html")

@base.route("/Animesvistos")
def animesvistos():
    animes = Animes.query.all()
    db.session.commit()
    print(animes)
    return render_template('animesvistos.html', animes= animes)



@base.route("/Animesvistos/create")
def create():
    return render_template("create.html")

@base.route("/Animesvistos/insert", methods=['POST'])
def insert():
    titulo = request.form.get('titulo')
    descripcion = request.form.get('descripcion')
    imagen = request.form.get("imagen")
    url = request.form.get("url")

    anime = Animes(titulo,descripcion,imagen,url)

    db.session.add(anime)
    db.session.commit()

    return redirect(url_for('base.animesvistos'))

@base.route("/Animesvistos/edit/<int:id>")
def edit(id):
    anime= Animes.query.get_or_404(id)
    return render_template('edit.html', anime=anime)

@base.route("/Animesvistos/update/<int:id>", methods=['POST'])
def update(id):
    anime= Animes.query.get_or_404(id)
    anime.titulo = request.form.get('titulo')
    anime.descripcion = request.form.get('descripcion')
    anime.imagen = request.form.get("imagen")
    anime.url = request.form.get("url")


    db.session.add(anime)
    db.session.commit()

    return redirect(url_for('base.animesvistos'))

@base.route("/Animesvistos/delete/<int:id>")
def delete(id):
    anime= Animes.query.get_or_404(id)

    db.session.delete(anime)
    db.session.commit()

    return redirect(url_for('base.animesvistos'))




