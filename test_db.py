import pytest
from models import *
import datetime
from datetime import datetime


def test_userdata1(test_client, init_db):
    user1 = db.session.query(userdata).filter(userdata.user_id == 1).first()
    assert user1.user_id == 1
    assert user1.role == "doctor"
    assert user1.email == "dinesh@gmail.com"
    assert user1.password == "123"


def test_userdata2(test_client, init_db):
    user2 = db.session.query(userdata).filter(userdata.user_id == 2).first()

    assert user2.user_id == 2
    assert user2.role == "patient"
    assert user2.email == "prabh@gmail.com"
    assert user2.password == "123"


def test_patient_model(test_client, init_db):
    patient1 = db.session.query(patient).filter(patient.patient_id == 2).first()

    assert patient1.patient_id == 2
    assert patient1.patient_name == "Prabhpreet Singh"
    assert patient1.address == "Prabhpreet Singh Address"
    assert patient1.age == 25
    assert patient1.gender == "Male"
    assert patient1.phone == "9876543210"


def test_doctor_model(test_client, init_db):
    doctor1 = db.session.query(doctor).filter(doctor.doctor_id == 1).first()

    assert doctor1.doctor_id == 1
    assert doctor1.doctor_name == "Dinesh Kumar"
    assert doctor1.year_exp == 10
    assert doctor1.speciality == "Cardiologist"
    assert doctor1.phone == "7894561230"
    assert doctor1.description == "Dinesh Kumar Description"
    assert doctor1.address == "Dinesh Kumar Address"


def test_prescription_model(test_client, init_db):
    presc = (
        db.session.query(prescription).filter(prescription.prescription_id == 1).first()
    )

    assert presc.prescription_id == 1
    assert presc.patient_id == 2
    assert presc.doctor_id == 1


def test_doseDirection_model(test_client, init_db):
    dose = (
        db.session.query(doseDirection)
        .filter(doseDirection.prescription_id == 1)
        .first()
    )

    assert dose.dose_id == 1
    assert dose.prescription_id == 1
    assert dose.dose == 2.5
    assert dose.dose_unit == "mg"
    assert dose.frequency_per_day == "3/d"


def test_orderDetails_model(test_client, init_db):
    order = (
        db.session.query(orderDetails).filter(orderDetails.prescription_id == 1).first()
    )

    assert order.orderdetails_id == 1
    assert order.prescription_id == 1
    assert order.status == "active"


def test_pastHistory_model(test_client, init_db):
    past_history = (
        db.session.query(pastHistoryIllness)
        .filter(pastHistoryIllness.patient_id == 2)
        .first()
    )

    assert past_history.illness_id == 1
    assert past_history.patient_id == 2
    assert past_history.problem_name == "Problem 1"
    assert past_history.body_site == "Arm"
    assert past_history.datetime_onset == datetime(2020, 11, 10, 10, 0, 0)


def test_allergyIntolerance_model(test_client, init_db):
    allergy = (
        db.session.query(allergyIntolerance)
        .filter(allergyIntolerance.patient_id == 2)
        .first()
    )

    assert allergy.allergy_id == 1
    assert allergy.patient_id == 2
    assert allergy.substance == "Lactose"
    assert allergy.verification_status == "Approved"
    assert allergy.allergy_intol_type == "allergy"


def test_problemList_model(test_client, init_db):
    problem = db.session.query(problemList).filter(problemList.patient_id == 2).first()

    assert problem.problem_id == 1
    assert problem.patient_id == 2
    assert problem.problem_diag_name == "Fever"
    assert problem.body_site == "Stomach"
