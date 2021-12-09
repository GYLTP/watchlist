from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import sys
from typing import Callable

# from sqlalchemy import *
# from sqlalchemy import Column
# from sqlalchemy import Integer


class MySQLAlchemy(SQLAlchemy):  # Or you can add the below code on the SQLAlchemy directly if you think to modify the package code is acceptable.
    Column: Callable  # Use the typing to tell the IDE what the type is.
    String: Callable
    Integer: Callable

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = MySQLAlchemy(app) # 在这里申明了db是对al的引用




@app.route('/')
def index():
    user = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html',name=user,movies=movies)


class User(db.Model): # 继承了db的方法
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


import click # 这个干什么？

@app.cli.command() #从app的路由模块创建
@click.option('--drop',is_flag=True, help='Create after drop') # 这个是增加选择
def initdb(drop):
    if drop:
        db.drop_all() # 相当于先删掉再创建
    db.create_all()
    click.echo('启动数据')


# 创建虚拟数据


@app.cli.command()
def forge():
    db.create_all()

    name = 'gao'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork 1of111 Music', 'year': '2012'},
    ]

    user = User(name = name )
    db.session.add(user) # 注意都要提交一次
    for m in movies:
        movie = Movie(title = m["title"],year = m["year"])
        db.session.add(movie)

    db.session.commit()
    click.echo('write done')
    # 注意这里的db需要自己构造一下 后续考虑上传git
    # 这里涉及到极少量的表关联















