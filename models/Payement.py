from config import db

class Payement(db.Model):
    amount = db.Column(db.Float, nullable = True)
    payementMode=""
    __mapper_args__={'polymorphique_on':payementMode}
