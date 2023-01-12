from anime import db

class AnimesNuevos(db.Model):
    __tablename__ = 'animesNuevos'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    descripcion = db.Column(db.String(100))
    imagen = db.Column(db.String(1000))
    url = db.Column(db.String(1000))

    def __init__(self,titulo,descripcion,imagen,url):
        self.titulo = titulo
        self.descripcion = descripcion
        self.imagen = imagen
        self.url = url
