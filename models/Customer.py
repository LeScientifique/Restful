from config import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(120), nullable = True)
    deliveryAddress = db.Column(db.String(120), nullable = True)
    contact = db.Column(db.String(120), nullable = True)
    active = db.Column(db.Boolean, nullable = True)
