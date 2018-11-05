#encoding=utf-8
__author__ = 'miaoshasha'
import os
#dialect+driver://username:password@host:port/database
DIALECT='mysql'
DRIVER='mysqldb'
USERNAME='root'
PASSWORD='root'
HOST='127.0.0.1'
PORT='3306'
DATABASE='movie'
DR_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI=DR_URI
SQLALCHEMY_TRACK_MODIFICATIONS=True