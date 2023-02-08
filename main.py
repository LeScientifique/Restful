import pymysql
from app import app
from config import db
from flask import jsonify,Flask,request,render_template,flash

with app.app_context():
    db.create_all()



if(__name__ == '__main__'):
    app.run()
