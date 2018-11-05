#encoding=utf-8
__author__ = 'miaoshasha'
from flask import Flask,render_template,request
from exts import db
import  config
from models import MovieActor
from operator import itemgetter
import operator
app = Flask (__name__)
db.init_app(app)
app.config.from_object(config)
@app.route ('/',methods=['POST','GET'])
def index():
    movies = MovieActor.query.filter ().limit (10)
    if request.method=='GET':
        return render_template ('index.html', movies=movies)
    else:
        cast=request.form.get('cast')
        m=MovieActor.query.filter (MovieActor.casts.ilike('%'+cast+'%')).all()
        return render_template ('index.html', movies=m)
@app.route('/relationship',methods=['POST','GET'])
def relationship():
    if request.method == 'GET':
        cast=request.args.get('cast')
        if cast:
            d=luoji (cast)
            return render_template ('relationship.html', relations=d)
        else:
            return render_template ('relationship.html')
    else:
        cast = request.form.get ('cast')
        d=luoji(cast)
        return render_template ('relationship.html', relations=d)
def luoji(cast):
    actors = MovieActor.query.filter (MovieActor.casts.ilike ('%' + cast + '%')).all ()
    c = []
    b = []
    for actor in actors:
        b = actor.casts.split (",")
        print b
        for i in range (0, len (b)):
            c.append (b[i])
            for i in range (0, len (c)):
                if c[i] == cast:
                    del c[i]
    m = list (set (c))
    # b = {}
    d = []
    for i in range (0, len (m)):
        d.append ({'caster': m[i], 'count': c.count (m[i])})
    d = sorted (d, key=operator.itemgetter ('count'), reverse=True)
    return d
if __name__ == '__main__':
    app.run ()
