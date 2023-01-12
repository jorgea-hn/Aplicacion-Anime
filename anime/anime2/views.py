from flask import render_template, Blueprint, request,redirect,url_for
from anime.anime2.model import AnimesNuevos

from anime import db

anime2 = Blueprint('anime2',__name__)

@anime2.route("/Animesporver")
def animesporver():
    animes = AnimesNuevos.query.all()
    db.session.commit()
    print(animes)
    return render_template('anime2/animesporver.html', animes= animes)



@anime2.route("/Animesporver/create")
def createporver():
    return render_template("anime2/createporver.html")

@anime2.route("/Animesporver/insert", methods=['POST'])
def insertporver():
    titulo = request.form.get('titulo')
    descripcion = request.form.get('descripcion')
    imagen = request.form.get("imagen")
    url = request.form.get("url")

    anime = AnimesNuevos(titulo,descripcion,imagen,url)

    db.session.add(anime)
    db.session.commit()

    return redirect(url_for('anime2.animesporver'))

@anime2.route("/Animesporver/edit/<int:id>")
def editporver(id):
    anime= AnimesNuevos.query.get_or_404(id)
    return render_template('anime2/editporver.html', anime=anime)


@anime2.route("/Animesporver/update/<int:id>", methods=['POST'])
def updateporver(id):
    anime= AnimesNuevos.query.get_or_404(id)
    anime.titulo = request.form.get('titulo')
    anime.descripcion = request.form.get('descripcion')
    anime.imagen = request.form.get("imagen")
    anime.url = request.form.get("url")


    db.session.add(anime)
    db.session.commit()

    return redirect(url_for('anime2.animesporver'))

@anime2.route("/Animesporver/delete/<int:id>")
def deleteporver(id):
    anime= AnimesNuevos.query.get_or_404(id)

    db.session.delete(anime)
    db.session.commit()

    return redirect(url_for('anime2.animesporver'))