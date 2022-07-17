from flask import Flask, render_template, redirect, request
from rooms import db, Room

app = Flask(__name__)
app.secret_key = 'xyz'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)


@app.route("/")
def index():
    room = Room.query.order_by(Room.id.desc()).all()
    return render_template("index.html", room=room)


@app.route("/add",  methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        room_n = request.form['name_room']
        room = Room(room_name=room_n, lights=1)
        try:
            if room:
                db.session.add(room)
                db.session.commit()

                return redirect('/')

            else:
                return redirect('/add')

        except:
            return "Error adding"

    else:
        return render_template("add.html")


@app.route("/<int:id>", methods=['POST', 'GET'])
def on_off(id):
    room = Room.query.get(id)
    if room.lights == 1:
        room.lights = 0
    elif room.lights == 0:
        room.lights = 1
    try:
        db.session.commit()
        return redirect('/')

    except:
        return "You have some error"
    return redirect("/")


app.run(host='localhost', port=5000)
