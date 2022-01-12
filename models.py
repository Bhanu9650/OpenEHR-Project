from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#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 Github Token

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:test@localhost/eapr"

db = SQLAlchemy(app) 
class userdata(db.Model):
    __tablename__ = 'userdata'
    userid = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20),unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), unique = False, nullable=False)



class patient(db.Model):
    __tablename__ = 'patient'

    pid = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(100), nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('userdata.userid'))
    date_of_reg =db.Column(db.DateTime,nullable = True)
    address=db.Column(db.String(100),nullable=False)
    age=db.Column(db.Integer,nullable = False)
    gender=db.Column(db.String(10), nullable=False)
    symptoms =db.Column(db.String(100), nullable=True)
    phone =db.Column(db.Integer,unique = True)
    doc_id = db.Column(db.Integer, nullable=True)



class doctor(db.Model):
    __tablename__ = 'doctor'
    doc_id =  db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('userdata.userid'))
    dname = db.Column(db.String(100), nullable=False)
    yoe= db.Column(db.Integer,unique = False)
    speciality=db.Column(db.String(100), nullable=False)
    phone =db.Column(db.Integer,unique = True)
    fee=phone =db.Column(db.Integer)
    availability_from = db.Column(db.String,nullable = True)
    availability_to  =db.Column(db.String,nullable = True)
    description =db.Column(db.String(100), nullable=False)
    address= db.Column(db.String(100), nullable=False)

    
class pharma(db.Model):
    __tablename__ = 'pharma'
    ph_id =db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('userdata.userid'))
    phname =db.Column(db.String(100), nullable=False)
    yoe = db.Column(db.Integer,unique = False)
    phone_no = db.Column(db.Integer,unique = True)
    address= db.Column(db.String(100), nullable=False)
    registration_no  = db.Column(db.String(100), nullable=False)

    
   
