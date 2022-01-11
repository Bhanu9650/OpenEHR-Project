from ctypes import addressof
from os import uname
import re
from flask import Flask, app, request
from flask.templating import render_template
from models import *
from models import userdata
import hashlib


from sqlalchemy import func 




db.create_all()
db.session.commit()


# app = Flask(__name__)


#Test Routes with /test Route  
@app.route('/test')
def test():
    return render_template('index.html')


#Renders Home Page
@app.route('/')
def home():
    return render_template('home.html')


#Renders SignIn Page
@app.route('/signin')
def login():
    return render_template('login.html')


#Renders Doctor SignUp Page
@app.route('/doctorsignup')
def dregister():
    return render_template('register2.html')

#Renders Pharmacist SignUp Page
@app.route('/pharmasignup')
def phregister():
    return render_template('register1.html')


#Renders Pharmacist SignUp Page
@app.route('/patientsignup')
def pregister():
    return render_template('register.html')



#Renders the Welcome Page
@app.route('/welcome', methods=["POST"])
def loginsucess():

    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('psw')
        # print(uname)
        # print(password)
        
        # print(g_name)
        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        result = db.session.query(userdata).filter(userdata.email==email, userdata.password==hashedPassword)
        
        # roles = result.role
        # for row in result:
        #     roles = row.role
       
        for row in result:
            if len(row.email)!= 0:
                roles = row.role          
                return render_template('welcome.html',data = roles )
        data = "Wrong credentials"
        return render_template('login.html',data = data)
        


#Renders Login Page After Registration
@app.route('/patientregistrationsuccess', methods=["POST"])
def registration():

    if request.method == "POST":
        pname = request.form.get('uname')
        email = request.form.get('mail')
        password = request.form.get('psw')
        address = request.form.get('add')
        age = request.form.get('age')
        gender = request.form.get('gen')
        phone = request.form.get('phn')
        (useriddata,)= db.session.query(func.max(userdata.userid)).first()
        # print(uname)
        # print(email)
        # print(password)
        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        entry = userdata(role = 'Patient',email = email,password = hashedPassword)
        
        entry1 = patient(pname = pname, age = age,gender = gender,address = address,phone = phone,userid = useriddata)
        db.session.add(entry)
        
        db.session.add(entry1)
        db.session.commit()
        return render_template('login.html')



@app.route('/pharmaregistrationsuccess', methods=["POST"])
def registration1():

    if request.method == "POST":
        pname = request.form.get('uname')
        email = request.form.get('mail')
        password = request.form.get('psw')
        address = request.form.get('add')
        phone = request.form.get('phn')
        yoe = request.form.get('yoe')
        regno = request.form.get('rn')
        # print(uname)
        # print(email)
        # print(password)
        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        entry = userdata(role = 'Pharmacist',email = email,password = hashedPassword)
        db.session.add(entry)
        (useriddata,)= db.session.query(func.max(userdata.userid)).first()
        entry1 = pharma(phname = pname,address = address,phone_no = phone,registration_no= regno,yoe = yoe,userid = useriddata )
        db.session.add(entry1)
        db.session.commit()
        return render_template('login.html')


@app.route('/doctorregistrationsuccess', methods=["POST"])
def registration2():

    if request.method == "POST":
        dname = request.form.get('uname')
        email = request.form.get('mail')
        password = request.form.get('psw')
        address = request.form.get('add')
        phone = request.form.get('phn')
        speciality = request.form.get('spl')
        fee = request.form.get('fee')
        yoe = request.form.get('yoe')
        desc = request.form.get('desc')
        avf = request.form.get('avf')
        avt = request.form.get('avt')
        (useriddata,)= db.session.query(func.max(userdata.userid)).first()

        # print(uname)
        # print(email)
        # print(password)
        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        entry = userdata(role = 'Doctor',email = email,password = hashedPassword)
        db.session.add(entry)
        
        entry1 = doctor(dname = dname,address = address,phone = phone,description= desc,yoe = yoe,speciality = speciality,fee = fee,availability_from = avf , availability_to = avt,userid = useriddata)
        db.session.add(entry1)
        db.session.commit()
        return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True, port=4005)
    


