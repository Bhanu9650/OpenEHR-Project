from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:abc123@localhost/eapr"

db = SQLAlchemy(app)


class userdata(db.Model):
    __tablename__ = "userdata"
    userid = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)


class patient(db.Model):
    __tablename__ = "patient"

    pid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey("userdata.userid"))
    doc_id = db.Column(db.Integer, db.ForeignKey("doctor.doc_id"), nullable=False)

    pname = db.Column(db.String(100), nullable=False)
    date_of_reg = db.Column(db.DateTime, nullable=True)
    address = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    symptoms = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.Integer, unique=True)


class doctor(db.Model):
    __tablename__ = "doctor"
    doc_id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey("userdata.userid"))

    dname = db.Column(db.String(100), nullable=False)
    yoe = db.Column(db.Integer, unique=False)
    speciality = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, unique=True)
    fee = db.Column(db.Integer, nullable=True)
    availability_from = db.Column(db.String, nullable=True)
    availability_to = db.Column(db.String, nullable=True)
    description = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)


class pharma(db.Model):
    __tablename__ = "pharma"
    ph_id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey("userdata.userid"))

    phname = db.Column(db.String(100), nullable=False)
    yoe = db.Column(db.Integer, unique=False)
    phone_no = db.Column(db.Integer, unique=True)
    address = db.Column(db.String(100), nullable=False)
    registration_no = db.Column(db.String(100), nullable=False)


# master table for "prescription"
# prescription:
#   subtables:
#     dosaDirection
#     orderDetails
#   linked tables:
#     pastHistoryIllness
#     allergyIntolerance
#     problemDiagnosis
class prescription(db.Model):
    __tablename__ = "prescription"

    prescription_id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.pid"), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctor.doc_id"), nullable=False)

    medication_item = db.Column(db.String(100), nullable=True)
    route = db.Column(db.String(50), nullable=True)
    dosage_instruction = db.Column(db.String(50), nullable=True)
    additional_instruction = db.Column(db.String(250), nullable=True)
    reason = db.Column(db.String(250), nullable=True)


# subtables
class doseDirection(db.Model):
    __tablename__ = "doseDirection"
    dose_id = db.Column(db.Integer, primary_key=True)
    prescription_id = db.Column(
        db.Integer, db.ForeignKey("prescription.prescription_id"), nullable=False
    )

    dose = db.Column(db.Float, nullable=False)
    dose_unit = db.Column(db.String(10), nullable=False)
    frequency_per_day = db.Column(db.Integer, nullable=False)


class orderDetails(db.Model):
    __tablename__ = "orderDetails"
    orderdetails_id = db.Column(db.Integer, primary_key=True)
    prescription_id = db.Column(
        db.Integer, db.ForeignKey("prescription.prescription_id"), nullable=False
    )

    status = db.Column(db.String(10), nullable=False)
    date_discontinued = db.Column(db.Date, nullable=False)  # datetime.Date obj
    date_written = db.Column(db.Date, nullable=False)


# Linked tables
class pastHistoryIllness(db.Model):
    __tablename__ = "pastHistoryIllness"
    illness_id = db.Column(db.Integer, primary_key=True)
    prescription_id = db.Column(
        db.Integer, db.ForeignKey("prescription.prescription_id"), nullable=False
    )

    problem_name = db.Column(db.String(100), nullable=False)
    body_site = db.Column(db.String(100), nullable=False)
    datetime_onset = db.Column(db.DateTime, nullable=False)
    severity = db.Column(db.String(50), nullable=True)
    procedure_type = db.Column(
        db.String(100), nullable=True
    ) 


class allergyIntolerance(db.Model):
    __tablename__ = "allergyIntolerance"
    allergy_id = db.Column(db.Integer, primary_key=True)
    prescription_id = db.Column(
        db.Integer, db.ForeignKey("prescription.prescription_id"), nullable=False
    )

    substance = db.Column(db.String(250), nullable=False)
    verification_status = db.Column(db.String(25), nullable=False)
    allergy_intol_type = db.Column(db.String(25), nullable=False)
    comment = db.Column(db.String(250), nullable=True)
    manifestation = db.Column(db.String(300), nullable=True)


class problemList(db.Model):
    __tablename__ = "problemDiagnosis"
    problem_id = db.Column(db.Integer, primary_key=True)
    prescription_id = db.Column(
        db.Integer, db.ForeignKey("prescription.prescription_id"), nullable=False
    )

    problem_diag_name = db.Column(db.String(100), nullable=False)
    body_site = db.Column(db.String(50), nullable=False)
    datetime_onset = db.Column(db.DateTime, nullable=True)
    severity = db.Column(db.String(25), nullable=True)
