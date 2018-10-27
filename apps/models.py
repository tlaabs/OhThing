"""
models.py

"""

from apps import db

class User(db.Model):
	room_id = db.Column(db.String(255), primary_key = True)
	available = db.Column(db.String(255))


