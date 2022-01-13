from ctypes import addressof
from os import uname
import re
from flask import Flask, app, request,jsonify,redirect,url_for
from flask.templating import render_template
from sqlalchemy.sql.functions import user
from models import *
from models import userdata
import hashlib


from sqlalchemy import func 
import json




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
@app.route('/dashboard', methods=["POST"])
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
                print(roles)
                userid = row.user_id
                return redirect(url_for('userHomePage', user_id=userid, role=roles))
            else:
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
        # print(uname)
        # print(email)
        # print(password)
        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        entry = userdata(role = 'Patient',email = email,password = hashedPassword)
        db.session.add(entry)
        (useriddata,)= db.session.query(func.max(userdata.user_id)).first()
        entry1 = patient(patient_name = pname, age = age,gender = gender,address = address,phone = phone,patient_id = useriddata)
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
        (useriddata,)= db.session.query(func.max(userdata.user_id)).first()
        entry1 = pharma(pharma_name = pname,address = address,phone_no = phone,registration_no= regno,year_exp = yoe,pharma_id = useriddata )
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

        # print(uname)
        # print(email)
        # print(password)
        hashedPassword = hashlib.md5(bytes(str(password),encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        entry = userdata(role = 'Doctor',email = email,password = hashedPassword)
        db.session.add(entry)
        (useriddata,)= db.session.query(func.max(userdata.user_id)).first()
        entry1 = doctor(doctor_name = dname,address = address,phone = phone,description= desc,year_exp = yoe,speciality = speciality,fee = fee,doctor_id= useriddata)
        db.session.add(entry1)
        db.session.commit()
        return render_template('login.html')


@app.route('/<role>/<user_id>', methods=["GET", "POST"])
def userHomePage(role, user_id):
    if role == 'Doctor':
        # role = role.capitalize()
        return render_template('doctorDashboard.html', data=role)
    elif role == 'Patient':
        return render_template('patientDashboard.html', data=role)
    else:
        return render_template('pharmaDashboard.html', data=role)


@app.route('/doctor/<doctor_id>/users', methods=["GET"])
def doctorUsersPage(doctor_id):
    pass
    
@app.route('/doctor/<doctor_id>/profile', methods=["GET"])
def doctorProfilePage(doctor_id):
    doctor_profile = db.session.query(doctor).filter(doctor.doc_id == doctor_id)
    doc_id = None
    email = None
    for row in doctor_profile:
        doc_id = row.userid
        break
    usr_id = db.session.query(userdata).filter(userdata.userid == doc_id)
    for row in usr_id:
        email = row.email
        break
    
    return jsonify([{'name':doc.dname,'phone':doc.phone,'address':doc.address,'speciality': doc.speciality,'description':doc.description,'email':email}
    for doc in doctor.query.filter(doctor.doc_id == doctor_id)
    ])


@app.route('/doctor/<doctor_id>/prescribe', methods=["GET"])
def doctorPrescribePage(doctor_id):
    pass
    
@app.route('/doctor/<doctor_id>/prescribe/prescription', methods=["POST"])
def doctorPrescriptionPage(doctor_id):
    pass
    
@app.route('/doctor/<doctor_id>/prescribe/past_illness', methods=["POST"])
def doctorPastIllnessPage(doctor_id):
    pass

@app.route('/doctor/<doctor_id>/prescribe/medication_summary', methods=["POST"])
def doctorMedicalIllnessPage(doctor_id):
    pass

@app.route('/doctor/<doctor_id>/prescribe/diagnosis', methods=["POST"])
def doctorDiagnosisPage(doctor_id):
    pass
    
    
@app.route('/patient/<patient_id>/profile', methods=["GET"])
def patientProfilePage(patient_id):

    pass 
if __name__ == "__main__":
    app.run(debug=True, port=4005)
    


