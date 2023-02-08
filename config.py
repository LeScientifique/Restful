from app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SECRET_KEY']='root'

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://hans:5637@localhost/order-dba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)