from config import db
import enum
from sqlalchemy import Enum

class OrderStatus(db.Model,enum.Enum):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    CREATE = db.Column(db.Integer, nullable = True)
    SHIPPING = db.Column(db.Integer, nullable = True)
    DELIVERED = db.Column(db.Integer, nullable = True)
    PAID = db.Column(db.Integer, nullable = True)

    orderId = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable = True)
    order = db.relationship('Orders', foreign_keys = [orderId])