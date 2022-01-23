import pytest


def test_home_page(test_client):
    response = test_client.get('/')
    assert response.status_code == 200

def test_signin_page(test_client):
    response = test_client.get('/signin')
    assert response.status_code == 200

def test_doctor_signup_page(test_client):
    response = test_client.get('/doctorsignup')
    assert response.status_code == 200

def test_patient_signup_page(test_client):
    response = test_client.get('/patientsignup')
    assert response.status_code == 200

def test_pharma_signup_page(test_client):
    response = test_client.get('/pharmasignup')
    assert response.status_code == 200

def test_home_page_invalid(test_client):
    response = test_client.get('/')
    assert not response.status_code == 404

def test_signin_page_invalid(test_client):
    response = test_client.get('/signin')
    assert not response.status_code == 404

def test_doctor_signup_page_invalid(test_client):
    response = test_client.get('/doctorsignup')
    assert not response.status_code == 404

def test_patient_signup_page_invalid(test_client):
    response = test_client.get('/patientsignup')
    assert not response.status_code == 404

def test_pharma_signup_page_invalid(test_client):
    response = test_client.get('/pharmasignup')
    assert not response.status_code == 404
