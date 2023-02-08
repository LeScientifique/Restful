from config import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    qty = db.Column(db.Integer, nullable = True)
    taxStatus = db.Column(db.String, nullable = True)

    def calculateSubTotal():
        ''

    def calculateWeight():
        ''