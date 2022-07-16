from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(100))
    lights = db.Column(db.Integer)


def __init__(self, room_name, lights):
    self.room_name = room_name
    self.lights = lights
