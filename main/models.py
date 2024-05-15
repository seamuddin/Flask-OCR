from main import db
from datetime import datetime

class Voter(db.Model):
    __tablename__ = 'voter_info'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    si = db.Column(db.String)
    name = db.Column(db.String)
    fathers_or_husband = db.Column(db.String)
    mother = db.Column(db.String)
    birth_date = db.Column(db.String)
    division = db.Column(db.String)
    district = db.Column(db.String)
    union = db.Column(db.String)
    election_area = db.Column(db.String)
    voter_no = db.Column(db.String)
    created_at = db.Column(db.String, default=datetime.now)
    updated_at = db.Column(db.String, default=datetime.now, onupdate=datetime.now)
    created_by = db.Column(db.String , default='0')
    updated_by = db.Column(db.String, default='0')
    upazila = db.Column(db.String, default='0')

    def _init_(self, name, email):
        self.name = name
