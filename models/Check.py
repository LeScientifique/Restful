from config import db
from Payement import Payement

class Check(db.Model,Payement):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String, nullable = True)
    bankID = db.Column(db.String, nullable = True)
    
    __mapper_args__={'polymorphique_on':'Check'}
