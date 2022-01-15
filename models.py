from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json, sys

try:
    with open(".config.json") as f:
        config = json.loads(f.read())
except FileNotFoundError:
    print("=" * 20)
    message = """Create file .config.json
    Set values as:
    {
        "DB":
        {
            "DB_USER": "",
            "DB_PWD": ""
        }
    }
    """
    print(message)
    sys.exit(0)

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{config['DB']['DB_USER']}:{config['DB']['DB_PWD']}@localhost/eapr"

db = SQLAlchemy(app)


class userdata(db.Model):
    __tablename__ = "userdata"
    user_id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)


class patient(db.Model):
    __tablename__ = "patient"

    _id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("userdata.user_id"), unique=True)
    # doctor_id = db.Column(db.Integer, db.ForeignKey("doctor.doctor_id"), nullable=True)
    # user_id = patient id , pid = _id

    patient_name = db.Column(db.String(100), nullable=False)
    date_of_reg = db.Column(db.DateTime, nullable=True)
    address = db.Column(db.String(250), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    symptoms = db.Column(db.String(250), nullable=True)
    phone = db.Column(db.String(15), unique=True)


class doctor(db.Model):
    __tablename__ = "doctor"
    _id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey("userdata.user_id"), unique=True)

    doctor_name = db.Column(db.String(100), nullable=False)
    year_exp = db.Column(db.Integer, unique=False)
    speciality = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), unique=True)
    fee = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(250), nullable=False)
    address = db.Column(db.String(250), nullable=False)


class pharma(db.Model):
    __tablename__ = "pharma"
    _id = db.Column(db.Integer, primary_key=True)
    pharma_id = db.Column(
        db.Integer, db.ForeignKey("userdata.user_id"), nullable=True, unique=True
    )

    pharma_name = db.Column(db.String(100), nullable=False)
    year_exp = db.Column(db.Integer, unique=False)
    phone_no = db.Column(db.String(15), unique=True)
    address = db.Column(db.String(250), nullable=False)
    registration_no = db.Column(db.String(100), unique=True, nullable=False)


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
    patient_id = db.Column(
        db.Integer, db.ForeignKey("patient.patient_id"), nullable=False
    )
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctor.doctor_id"), nullable=False)

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
    frequency_per_day = db.Column(db.String(100), nullable=False)  ## eg 1;1\d and 5;1\w


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
    patient_id = db.Column(
        db.Integer, db.ForeignKey("patient.patient_id"), nullable=False
    )

    problem_name = db.Column(db.String(100), nullable=False)
    body_site = db.Column(db.String(100), nullable=False)
    datetime_onset = db.Column(db.DateTime, nullable=False)
    severity = db.Column(db.String(50), nullable=True)
    procedure_type = db.Column(db.String(100), nullable=True)


class allergyIntolerance(db.Model):
    __tablename__ = "allergyIntolerance"
    allergy_id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(
        db.Integer, db.ForeignKey("patient.patient_id"), nullable=False
    )

    substance = db.Column(db.String(250), nullable=False)
    verification_status = db.Column(db.String(25), nullable=False)
    allergy_intol_type = db.Column(db.String(25), nullable=False)
    comment = db.Column(db.String(250), nullable=True)
    manifestation = db.Column(db.String(300), nullable=True)


class problemList(db.Model):
    __tablename__ = "problemList"
    problem_id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(
        db.Integer, db.ForeignKey("patient.patient_id"), nullable=False
    )

    problem_diag_name = db.Column(db.String(100), nullable=False)
    body_site = db.Column(db.String(50), nullable=False)
    datetime_onset = db.Column(db.DateTime, nullable=True)
    severity = db.Column(db.String(25), nullable=True)
