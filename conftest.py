from flask_login import fresh_login_required
import pytest
from models import *
from datetime import datetime


@pytest.fixture(scope="module")
def test_client():

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_db.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["TESTING"] = True
    # Creating test client
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


@pytest.fixture(scope="module")
def init_db(test_client):
    db.create_all()

    users_doc = userdata(
        user_id=1, role="doctor", email="dinesh@gmail.com", password="123"
    )
    users_pat = userdata(
        user_id=2, role="patient", email="prabh@gmail.com", password="123"
    )
    doctor1 = doctor(
        _id=1,
        doctor_id=1,
        doctor_name="Dinesh Kumar",
        year_exp=10,
        speciality="Cardiologist",
        phone="7894561230",
        description="Dinesh Kumar Description",
        address="Dinesh Kumar Address",
    )

    patient1 = patient(
        _id=1,
        patient_id=2,
        patient_name="Prabhpreet Singh",
        address="Prabhpreet Singh Address",
        age=25,
        gender="Male",
        phone="9876543210",
    )

    presc = prescription(prescription_id=1, patient_id=2, doctor_id=1)

    doseDir = doseDirection(
        dose_id=1, prescription_id=1, dose=2.5, dose_unit="mg", frequency_per_day="3/d"
    )

    order = orderDetails(
        orderdetails_id=1,
        prescription_id=1,
        status="active",
        date_discontinued=datetime(2020, 11, 10),
        date_written=datetime(2021, 10, 1),
    )

    pastHis = pastHistoryIllness(
        illness_id=1,
        patient_id=2,
        problem_name="Problem 1",
        body_site="Arm",
        datetime_onset=datetime(2020, 11, 10, 10, 0, 0),
    )

    allergy = allergyIntolerance(
        allergy_id=1,
        patient_id=2,
        substance="Lactose",
        verification_status="Approved",
        allergy_intol_type="allergy",
    )

    problem = problemList(
        problem_id=1, patient_id=2, problem_diag_name="Fever", body_site="Stomach"
    )

    db.session.add(users_doc)
    db.session.add(users_pat)

    db.session.add(doctor1)
    db.session.add(patient1)

    db.session.add(presc)
    db.session.add(doseDir)
    db.session.add(order)

    db.session.add(pastHis)
    db.session.add(allergy)
    db.session.add(problem)

    db.session.commit()

    yield

    db.drop_all()
