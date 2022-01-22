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


def test_userdata1_invalid_role(test_client, init_db):
    user1 = db.session.query(userdata).filter(userdata.user_id == 1).first()
    assert user1.user_id == 1
    assert not user1.role == "patient"
    assert user1.email == "dinesh@gmail.com"
    assert user1.password == "123"


def test_userdata1_invalid_email(test_client, init_db):
    user1 = db.session.query(userdata).filter(userdata.user_id == 1).first()
    assert user1.user_id == 1
    assert user1.role == "doctor"
    assert not user1.email == "prabh@gmail.com"
    assert user1.password == "123"


def test_userdata2(test_client, init_db):
    user2 = db.session.query(userdata).filter(userdata.user_id == 2).first()

    assert user2.user_id == 2
    assert user2.role == "patient"
    assert not user2.email == "dinesh@gmail.com"
    assert user2.password == "123"


def test_userdata2_invalid_role(test_client, init_db):
    user2 = db.session.query(userdata).filter(userdata.user_id == 2).first()

    assert user2.user_id == 2
    assert not user2.role == "doctor"
    assert user2.email == "prabh@gmail.com"
    assert user2.password == "123"


def test_userdata2_invalid_email(test_client, init_db):
    user2 = db.session.query(userdata).filter(userdata.user_id == 2).first()

    assert user2.user_id == 2
    assert user2.role == "patient"
    assert not user2.email == "dk@gmail.com"
    assert user2.password == "123"


def test_patient_model(test_client, init_db):
    patient1 = db.session.query(patient).filter(patient.patient_id == 2).first()

    assert patient1.patient_id == 2
    assert patient1.patient_name == "Prabhpreet Singh"
    assert patient1.address == "Prabhpreet Singh Address"
    assert patient1.age == 25
    assert patient1.gender == "Male"
    assert patient1.phone == "9876543210"


def test_patient_model_invalid(test_client, init_db):
    patient1 = db.session.query(patient).filter(patient.patient_id == 2).first()

    assert patient1.patient_id == 2
    assert not patient1.patient_name == "Dinesh Kumar"
    assert patient1.address == "Prabhpreet Singh Address"
    assert patient1.age == 25
    assert patient1.gender == "Male"
    assert patient1.phone == "9876543210"


def test_patient_model_invalid(test_client, init_db):
    patient1 = db.session.query(patient).filter(patient.patient_id == 2).first()

    assert patient1.patient_id == 2
    assert patient1.patient_name == "Prabhpreet Singh"
    assert patient1.address == "Prabhpreet Singh Address"
    assert patient1.age == 25
    assert patient1.gender == "Male"
    assert not patient1.phone == "654987123"


def test_doctor_model(test_client, init_db):
    doctor1 = db.session.query(doctor).filter(doctor.doctor_id == 1).first()

    assert doctor1.doctor_id == 1
    assert doctor1.doctor_name == "Dinesh Kumar"
    assert doctor1.year_exp == 10
    assert doctor1.speciality == "Cardiologist"
    assert doctor1.phone == "7894561230"
    assert doctor1.description == "Dinesh Kumar Description"
    assert doctor1.address == "Dinesh Kumar Address"


def test_doctor_model_invalid_name(test_client, init_db):
    doctor1 = db.session.query(doctor).filter(doctor.doctor_id == 1).first()

    assert doctor1.doctor_id == 1
    assert not doctor1.doctor_name == "Prabhpreet Singh"
    assert doctor1.year_exp == 10
    assert doctor1.speciality == "Cardiologist"
    assert doctor1.phone == "7894561230"
    assert doctor1.description == "Dinesh Kumar Description"
    assert doctor1.address == "Dinesh Kumar Address"


def test_doctor_model_invalid_phone(test_client, init_db):
    doctor1 = db.session.query(doctor).filter(doctor.doctor_id == 1).first()

    assert doctor1.doctor_id == 1
    assert doctor1.doctor_name == "Dinesh Kumar"
    assert doctor1.year_exp == 10
    assert doctor1.speciality == "Cardiologist"
    assert not doctor1.phone == "9876543210"
    assert doctor1.description == "Dinesh Kumar Description"
    assert doctor1.address == "Dinesh Kumar Address"


def test_prescription_model(test_client, init_db):
    presc = (
        db.session.query(prescription).filter(prescription.prescription_id == 1).first()
    )

    assert presc.prescription_id == 1
    assert presc.patient_id == 2
    assert presc.doctor_id == 1


def test_prescription_model_invalid_prescription_id(test_client, init_db):
    presc = (
        db.session.query(prescription).filter(prescription.prescription_id == 1).first()
    )

    assert not presc.prescription_id == 2
    assert presc.patient_id == 2
    assert presc.doctor_id == 1


def test_prescription_model_invalid_patient_id(test_client, init_db):
    presc = (
        db.session.query(prescription).filter(prescription.prescription_id == 1).first()
    )

    assert presc.prescription_id == 1
    assert not presc.patient_id == 1
    assert presc.doctor_id == 1


def test_prescription_model_invalid_doctor_id(test_client, init_db):
    presc = (
        db.session.query(prescription).filter(prescription.prescription_id == 1).first()
    )

    assert presc.prescription_id == 1
    assert presc.patient_id == 2
    assert not presc.doctor_id == 2


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


def test_doseDirection_model_invalid_dose_id(test_client, init_db):
    dose = (
        db.session.query(doseDirection)
        .filter(doseDirection.prescription_id == 1)
        .first()
    )

    assert not dose.dose_id == 2
    assert dose.prescription_id == 1
    assert dose.dose == 2.5
    assert dose.dose_unit == "mg"
    assert dose.frequency_per_day == "3/d"


def test_doseDirection_model_invalid_presc_id(test_client, init_db):
    dose = (
        db.session.query(doseDirection)
        .filter(doseDirection.prescription_id == 1)
        .first()
    )

    assert dose.dose_id == 1
    assert not dose.prescription_id == 1
    assert dose.dose == 2.5
    assert dose.dose_unit == "mg"
    assert dose.frequency_per_day == "3/d"


def test_doseDirection_model_invalid_dose_amt(test_client, init_db):
    dose = (
        db.session.query(doseDirection)
        .filter(doseDirection.prescription_id == 1)
        .first()
    )

    assert dose.dose_id == 1
    assert dose.prescription_id == 1
    assert not dose.dose == 2.5
    assert dose.dose_unit == "mg"
    assert dose.frequency_per_day == "3/d"


def test_doseDirection_model_invalid_units(test_client, init_db):
    dose = (
        db.session.query(doseDirection)
        .filter(doseDirection.prescription_id == 1)
        .first()
    )

    assert dose.dose_id == 1
    assert dose.prescription_id == 1
    assert dose.dose == 2.5
    assert not dose.dose_unit == "mg"
    assert dose.frequency_per_day == "3/d"


def test_orderDetails_model(test_client, init_db):
    order = (
        db.session.query(orderDetails).filter(orderDetails.prescription_id == 1).first()
    )

    assert order.orderdetails_id == 1
    assert order.prescription_id == 1
    assert order.status == "active"


def test_orderDetails_model_invalid_(test_client, init_db):
    order = (
        db.session.query(orderDetails).filter(orderDetails.prescription_id == 1).first()
    )

    assert not order.orderdetails_id == 2
    assert order.prescription_id == 1
    assert order.status == "active"


def test_orderDetails_model_invalid_presc_id(test_client, init_db):
    order = (
        db.session.query(orderDetails).filter(orderDetails.prescription_id == 1).first()
    )

    assert order.orderdetails_id == 1
    assert not order.prescription_id == 2
    assert order.status == "active"


def test_orderDetails_model_invalid_status(test_client, init_db):
    order = (
        db.session.query(orderDetails).filter(orderDetails.prescription_id == 1).first()
    )

    assert order.orderdetails_id == 1
    assert order.prescription_id == 1
    assert not order.status == "inactive"


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


def test_pastHistory_model_invalid_illness_id(test_client, init_db):
    past_history = (
        db.session.query(pastHistoryIllness)
        .filter(pastHistoryIllness.patient_id == 2)
        .first()
    )

    assert not past_history.illness_id == 2
    assert past_history.patient_id == 2
    assert past_history.problem_name == "Problem 1"
    assert past_history.body_site == "Arm"
    assert past_history.datetime_onset == datetime(2020, 11, 10, 10, 0, 0)


def test_pastHistory_model_invalid_patient_id(test_client, init_db):
    past_history = (
        db.session.query(pastHistoryIllness)
        .filter(pastHistoryIllness.patient_id == 2)
        .first()
    )

    assert past_history.illness_id == 1
    assert not past_history.patient_id == 1
    assert past_history.problem_name == "Problem 1"
    assert past_history.body_site == "Arm"
    assert past_history.datetime_onset == datetime(2020, 11, 10, 10, 0, 0)


def test_pastHistory_model_invalid_problem_name(test_client, init_db):
    past_history = (
        db.session.query(pastHistoryIllness)
        .filter(pastHistoryIllness.patient_id == 2)
        .first()
    )

    assert past_history.illness_id == 1
    assert past_history.patient_id == 2
    assert not past_history.problem_name == "Another Problem"
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


def test_allergyIntolerance_model_invalid_allergy_id(test_client, init_db):
    allergy = (
        db.session.query(allergyIntolerance)
        .filter(allergyIntolerance.patient_id == 2)
        .first()
    )

    assert not allergy.allergy_id == 2
    assert allergy.patient_id == 2
    assert allergy.substance == "Lactose"
    assert allergy.verification_status == "Approved"
    assert allergy.allergy_intol_type == "allergy"


def test_allergyIntolerance_model_invalid_patient_id(test_client, init_db):
    allergy = (
        db.session.query(allergyIntolerance)
        .filter(allergyIntolerance.patient_id == 2)
        .first()
    )

    assert allergy.allergy_id == 1
    assert not allergy.patient_id == 1
    assert allergy.substance == "Lactose"
    assert allergy.verification_status == "Approved"
    assert allergy.allergy_intol_type == "allergy"


def test_allergyIntolerance_model_invalid_verfi(test_client, init_db):
    allergy = (
        db.session.query(allergyIntolerance)
        .filter(allergyIntolerance.patient_id == 2)
        .first()
    )

    assert allergy.allergy_id == 1
    assert allergy.patient_id == 2
    assert allergy.substance == "Lactose"
    assert not allergy.verification_status == "rejected"
    assert allergy.allergy_intol_type == "allergy"


def test_problemList_model(test_client, init_db):
    problem = db.session.query(problemList).filter(problemList.patient_id == 2).first()

    assert problem.problem_id == 1
    assert problem.patient_id == 2
    assert problem.problem_diag_name == "Fever"
    assert problem.body_site == "Stomach"


def test_problemList_model_invalid_problem_id(test_client, init_db):
    problem = db.session.query(problemList).filter(problemList.patient_id == 2).first()

    assert not problem.problem_id == 2
    assert problem.patient_id == 2
    assert problem.problem_diag_name == "Fever"
    assert problem.body_site == "Stomach"


def test_problemList_model_invalid_patient_id(test_client, init_db):
    problem = db.session.query(problemList).filter(problemList.patient_id == 2).first()

    assert problem.problem_id == 1
    assert not problem.patient_id == 1
    assert problem.problem_diag_name == "Fever"
    assert problem.body_site == "Stomach"


def test_problemList_model_invalid_body_site(test_client, init_db):
    problem = db.session.query(problemList).filter(problemList.patient_id == 2).first()

    assert problem.problem_id == 1
    assert problem.patient_id == 2
    assert problem.problem_diag_name == "Fever"
    assert not problem.body_site == "arm"
