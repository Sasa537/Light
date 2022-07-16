from flask import Flask, render_template,redirect
from rooms import db

app = Flask(__name__)
app.secret_key = 'xyz'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///light.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)


#@app.before_first_request
#def create_all():
    #db.create_all()


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/add")
def add():

    return render_template("add.html")


app.run(host='localhost', port=5000)