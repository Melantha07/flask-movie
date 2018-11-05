#encoding=utf-8
__author__ = 'miaoshasha'
from exts import db
class MovieActor(db.Model):
    __tablename__='movie_actor'
    id=db.Column(db.String(64),primary_key=True)
    directors=db.Column(db.String(2000))
    title=db.Column(db.String(2000))
    rate=db.Column(db.String(11))
    casts=db.Column(db.String(2000))
    cover=db.Column(db.String(5000))