from config import db
from Payement import Payement

class Cash(db.Model,Payement):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    cashTenderer = db.Column(db.Float, nullable = True)
    
    __mapper_args__={'polymorphique_on':'Cash'}
