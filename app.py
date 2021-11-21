from flask import Flask, render_template
app = Flask(__name__)


name = 'mark'
movies = [
    {'title':'a','year':'1991'},
    {'title':'b','year':'1992'},
]

@app.route('/')
def index():
    return render_template('index.html',name=name,movies=movies)



