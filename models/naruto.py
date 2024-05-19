from app import db

class naruto(db.Model):
    __tablename__ = 'naruto'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    age = db.Column(db.Integer)
    rank = db.Column(db.String())
    sex  = db.Column(db.String())
    affiliation = db.Column(db.String())
    primary_chakra_nature = db.Column(db.String())
    secondary_chakra_nature = db.Column(db.String())
    genjutsu = db.Column(db.Integer)
    ninjutsu = db.Column(db.Integer)
    taijutsu = db.Column(db.Integer)