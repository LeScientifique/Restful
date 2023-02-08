from config import db
from Payement import Payement

class Credit(db.Model,Payement):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    number = db.Column(db.String, nullable = True)
    type = db.Column(db.String, nullable = True)
    expireDate = db.Column(db.Date, nullable = True)
    
    __mapper_args__={'polymorphique_identity':'Credit'}
