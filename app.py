from crypt import methods
from ctypes import addressof
from os import uname
import re
from flask import Flask, app, request, jsonify, redirect, url_for

from flask.templating import render_template
from sqlalchemy.sql.functions import user
from models import patient, problemList, prescription
from models import userdata
from models import *
from werkzeug.exceptions import HTTPException
import hashlib


from sqlalchemy import func
import json


db.create_all()
db.session.commit()


# app = Flask(__name__)


# Test Routes with /test Route
@app.route('/test')
def test():
    return render_template('index.html')


# Renders Home Page
@app.route('/')
def home():
    return render_template('home.html')


# Renders SignIn Page
@app.route('/signin')
def login():
    return render_template('login.html')


# Renders Doctor SignUp Page
@app.route('/doctorsignup')
def dregister():
    return render_template('register2.html')

# Renders Pharmacist SignUp Page


@app.route('/pharmasignup')
def phregister():
    return render_template('register1.html')


# Renders Pharmacist SignUp Page
@app.route('/patientsignup')
def pregister():
    return render_template('register.html')


# Renders the Welcome Page
@app.route('/dashboard', methods=["POST"])
def loginsucess():

    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('psw')
 
        hashedPassword = hashlib.md5(bytes(str(password), encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        result = db.session.query(userdata).filter(
            userdata.email == email, userdata.password == hashedPassword)

        # roles = result.role
        # for row in result:
        #     roles = row.role
        
        for row in result:
            if len(row.email)!= 0:
                roles = row.role.lower()
                userid = row.user_id
                return redirect(url_for('userHomePage', user_id=userid, role=roles))
            else:
                data = "Wrong credentials"
                return render_template('login.html',data = data)
    else:
        return render_template('login.html')
                

# Renders Login Page After Registration
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

        hashedPassword = hashlib.md5(bytes(str(password), encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        entry = userdata(role='patient', email=email, password=hashedPassword)
        db.session.add(entry)
        (useriddata,) = db.session.query(func.max(userdata.user_id)).first()
        entry1 = patient(patient_name=pname, age=age, gender=gender,
                         address=address, phone=phone, patient_id=useriddata)
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

        hashedPassword = hashlib.md5(bytes(str(password), encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        entry = userdata(role='pharmacist', email=email,
                         password=hashedPassword)
        db.session.add(entry)
        (useriddata,) = db.session.query(func.max(userdata.user_id)).first()
        entry1 = pharma(pharma_name=pname, address=address, phone_no=phone,
                        registration_no=regno, year_exp=yoe, pharma_id=useriddata)
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

        hashedPassword = hashlib.md5(bytes(str(password), encoding='utf-8'))
        hashedPassword = hashedPassword.hexdigest()
        entry = userdata(role='doctor', email=email, password=hashedPassword)
        db.session.add(entry)
        (useriddata,) = db.session.query(func.max(userdata.user_id)).first()
        entry1 = doctor(doctor_name=dname, address=address, phone=phone, description=desc,
                        year_exp=yoe, speciality=speciality, fee=fee, doctor_id=useriddata)
        db.session.add(entry1)
        db.session.commit()
        return render_template('login.html')


@app.route('/<role>/<user_id>', methods=["GET", "POST"])
def userHomePage(role, user_id):
    if role == 'doctor':
        prescription_data = db.session.query(prescription,patient).\
                            join(patient, prescription.patient_id == patient.patient_id).\
                            filter(prescription.doctor_id == user_id).all()
        return render_template('doctor/home.html', data=role, data2=user_id, prescription_data=prescription_data)
    elif role == 'patient':
        patient_data = db.session.query(prescription, patient, doctor)\
            .join(patient, prescription.patient_id == patient.patient_id)\
            .join(doctor, prescription.doctor_id == doctor.doctor_id)\
            .filter(prescription.patient_id == user_id)\
            .all()

        return render_template('patient/home.html', data=role, data2=user_id, patient_data= patient_data )
    else:
        return render_template('pharmaDashboard.html', data=role)

# We have to change users ---> patients
@app.route('/doctor/<doctor_id>/users', methods=["GET", "POST"])
def doctorUsersPage(doctor_id):
    patient_info = db.session.query(patient).all()
    return render_template('doctor/patientlist.html', patient_data = patient_info, data='doctor' , data2=doctor_id )


@app.route('/doctor/<doctor_id>/profile', methods=["GET"])
def doctorProfilePage(doctor_id):             
    doctor_profile = db.session.query(doctor).filter(doctor.doctor_id == doctor_id)
    doctor_info = None
    for doc_id in doctor_profile:
        doctor_info = doc_id
    return render_template('doctor/profile.html', doctor_info=doctor_info)

@ app.route('/doctor/<doctor_id>/prescribe', methods = ["GET", "POST"])
def doctorPrescribePage(doctor_id):
    return render_template('doctor/prescribe.html', data2=doctor_id)

@ app.route('/doctor/<doctor_id>/prescribe/prescription', methods = ["GET","POST"])
def doctorPrescriptionPage(doctor_id):
    if request.method == "GET":
        return render_template('doctor/form-prescription.html',data='doctor',data2=doctor_id)
    elif request.method == "POST":
        patient_id = request.form.get('patient_id')
        medication_item = request.form.get('medication_item')
        route = request.form.get('route')
        dosage_instruction = request.form.get('dosage_instruction')
        additional_instruction = request.form.get('additional_instruction')
        reason = request.form.get('reason')

        patient_detail = db.session.query(patient).filter_by(patient_id=patient_id).first()
        if patient_detail is not None:
            entry = prescription(patient_id=patient_id  , doctor_id = doctor_id, medication_item = medication_item, route=route,dosage_instruction=dosage_instruction, additional_instruction=additional_instruction, reason=reason)
            db.session.add(entry)
            db.session.commit()

            db.session.flush()


            prescription_id = entry.prescription_id
            dose = request.form.get('dose')
            dose_unit = request.form.get('dose_unit')
            frequency_per_day = request.form.get('frequency_per_day')
            status = request.form.get('status')
            date_discontinued = request.form.get('date_discontinued')
            date_written = request.form.get('date_written')

            entry1 = doseDirection(prescription_id=prescription_id, dose=dose, dose_unit=dose_unit, frequency_per_day=frequency_per_day)
            db.session.add(entry1)
            db.session.commit()

            entry2 = orderDetails(prescription_id=prescription_id, status=status, date_discontinued=date_discontinued, date_written=date_written)

            db.session.add(entry2)
            db.session.commit()
            return redirect(url_for('doctorPrescribePage',doctor_id=doctor_id))

        else:
            return render_template("doctor/form-prescription.html", data={"message":"Patient does not exist. Please check the Patient ID and try again."})


@app.route('/doctor/<doctor_id>/prescribe/past_illness', methods=["GET", "POST"])
def doctorPastIllnessPage(doctor_id):

    if request.method == "GET":
        return render_template("doctor/form-pastillness.html",data='doctor',data2=doctor_id)
    
    elif request.method == "POST":
        patient_id = request.form.get('patient_id')
        problem_name = request.form.get('problem_name')
        body_site = request.form.get('body_site')
        datetime_onset = request.form.get('datetime_onset')
        severity = request.form.get('severity')
        procedure_type = request.form.get('procedure_type')

        patient_details = db.session.query(patient).filter_by(patient_id=patient_id).first()
        if patient_details is not None:

            problem1 = db.session.query(pastHistoryIllness).filter_by(patient_id=patient_id).first()
            if problem1 is not None:
                entry1 = db.session.query(pastHistoryIllness).filter_by(patient_id=patient_id).update(
                    {
                        pastHistoryIllness.problem_name:request.form.get('problem_name'),
                        pastHistoryIllness.body_site:request.form.get('body_site'),
                        pastHistoryIllness.datetime_onset:request.form.get('datetime_onset'),
                        pastHistoryIllness.severity:request.form.get('severity') ,
                        pastHistoryIllness.procedure_type:request.form.get('procedure_type') 
                     })
                db.session.commit()
                return redirect(url_for('doctorPrescribePage', doctor_id=doctor_id))

            else:
                entry1 = pastHistoryIllness(patient_id=patient_id,
                                problem_name=problem_name,
                                body_site=body_site,
                                datetime_onset=datetime_onset,
                                severity=severity,
                                procedure_type=procedure_type
                                )
                db.session.add(entry1)
                db.session.commit()
                return redirect(url_for('doctorPrescribePage', doctor_id=doctor_id))

        else:
            message = {
                "message": "Patient does not exist. Please check the Patient ID and try again."
                }
    
            return render_template("doctor/form-pastillness.html", data=message)

@ app.route('/doctor/<doctor_id>/prescribe/allergy', methods = ["GET","POST"])
def doctorAllergyIntolerance(doctor_id):

    if request.method == "GET":
        return render_template("doctor/form-allergy.html",data='doctor',data2=doctor_id)
    
    elif request.method == "POST":
        patient_id = request.form.get('patient_id')
        substance = request.form.get('substance')
        verification_status = request.form.get('verification_status')
        allergy_intol_type = request.form.get('allergy_intol_type')
        comment = request.form.get('comment')
        manifestation = request.form.get('manifestation')

        patient_details = db.session.query(patient).filter_by(patient_id=patient_id).first()
        if patient_details is not None:
            
            problem1 = db.session.query(allergyIntolerance).filter_by(patient_id=patient_id).first()
            if problem1 is not None:
                entry1 = db.session.query(allergyIntolerance).filter_by(patient_id=patient_id).update(
                    {
                        allergyIntolerance.substance:request.form.get('substance'),
                        allergyIntolerance.verification_status:request.form.get('verification_status'),
                        allergyIntolerance.allergy_intol_type:request.form.get('allergy_intol_type'),
                        allergyIntolerance.comment:request.form.get('comment') ,
                        allergyIntolerance.manifestation:request.form.get('manifestation') 
                     })
                db.session.commit()
                return redirect(url_for('doctorPrescribePage', doctor_id=doctor_id))

            else:
                entry1 = allergyIntolerance(patient_id=patient_id,
                                substance=substance,
                                verification_status=verification_status,
                                allergy_intol_type=allergy_intol_type,
                                comment=comment,
                                manifestation=manifestation
                                )
                db.session.add(entry1)
                db.session.commit()
                return redirect(url_for('doctorPrescribePage', doctor_id=doctor_id))
        else:
            message = {
                "message": "Patient does not exist. Please check the Patient ID and try again."
                }
    
            return render_template("doctor/form-allergy.html", data=message)



@ app.route('/doctor/<doctor_id>/prescribe/diagnosis', methods = ["GET","POST"])
def doctorDiagnosisPage(doctor_id):
    if request.method == "GET":
        return render_template("doctor/form-problem.html",data='doctor',data2=doctor_id)
    elif request.method == "POST":
        patient_id = request.form.get('patient_id')
        problem_diag_name = request.form.get('problem_diag_name')
        body_site = request.form.get('body_site')
        datetime_onset = request.form.get('datetime_onset')
        severity = request.form.get('severity')

        patient_details = db.session.query(patient).filter_by(patient_id=patient_id).first()

        if patient_details is not None:
            problem1 = db.session.query(problemList).filter_by(patient_id=patient_id).first()
            if problem1 is not None:
                entry1 = db.session.query(problemList).filter_by(patient_id=patient_id).update(
                    {
                        problemList.problem_diag_name:request.form.get('problem_diag_name'),
                        problemList.body_site:request.form.get('body_site'),
                        problemList.datetime_onset:request.form.get('datetime_onset'),
                        problemList.severity:request.form.get('severity') 
                     })
                db.session.commit()
                return redirect(url_for('doctorPrescribePage', doctor_id=doctor_id))

            else:
                entry1 = problemList(patient_id=patient_id, problem_diag_name=problem_diag_name, body_site=body_site, datetime_onset=datetime_onset, severity=severity)
                db.session.add(entry1)
                db.session.commit()
                return redirect(url_for('doctorPrescribePage', doctor_id=doctor_id))

        else:

            return render_template("doctor/form-problem.html", data={"message":"Patient does not exist. Please check the Patient ID and try again."})


@ app.route('/doctor/<doctor_id>/patients/<patient_id>', methods=["GET"])
def patientSummary(doctor_id, patient_id):
    data = db.session.query(patient,pastHistoryIllness,allergyIntolerance, problemList).\
        join(pastHistoryIllness,patient.patient_id == pastHistoryIllness.patient_id).\
        join(allergyIntolerance,patient.patient_id == allergyIntolerance.patient_id).\
        join(problemList,patient.patient_id == problemList.patient_id).\
        filter(patient.patient_id == patient_id).first()

    print(data)
    return render_template('doctor/doctor_patient_summary.html',data1 = data, data='doctor' , data2=doctor_id  )


@ app.route('/patient/<patient_id>/profile', methods = ["GET","POST"])
def patientProfilePage(patient_id):
    patient_profile=db.session.query(patient).filter(patient.patient_id == patient_id)
  
    return render_template('patient/profile.html',data = 'patient', data2=patient_id, data1=patient_profile.first())
    

@ app.route('/patient/<patient_id>/<prescription_id>', methods = ["GET"])
def patientPresciptionPage(patient_id, prescription_id):
    total_prescription = db.session.query(prescription,doseDirection,orderDetails).\
        join(doseDirection,prescription.prescription_id == doseDirection.prescription_id).\
        join(orderDetails,prescription.prescription_id == orderDetails.prescription_id).\
        filter(prescription.patient_id == patient_id).filter(prescription.prescription_id==prescription_id).all()
    print("PRESCRIPTION:", total_prescription)
    return render_template ('doctor/doctor_prescription.html',data=total_prescription)

@ app.route('/doctor/<doctor_id>/<prescription_id>', methods = ["GET"])
def doctorPresciptionPage(doctor_id, prescription_id):
    total_prescription = db.session.query(prescription,doseDirection,orderDetails).\
        join(doseDirection,prescription.prescription_id == doseDirection.prescription_id).\
        join(orderDetails,prescription.prescription_id == orderDetails.prescription_id).\
        filter(prescription.prescription_id==prescription_id).all()
    # print("PRESCRIPTION:", total_prescription)
    
    return render_template ('doctor/doctor_prescription.html',data1=total_prescription,  data='doctor' , data2=doctor_id)



@app.errorhandler(Exception)
def handle_error(e):
    code = 404
    if isinstance(e, HTTPException):
        code = e.code
    return render_template('error404.html')

if __name__ == "__main__":
    app.run(debug = True, port = 4005)
