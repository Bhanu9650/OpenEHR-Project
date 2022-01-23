# Easy Access Patient Records
![example workflow](https://github.com/shruti-17/OpenEHR-Project/actions/workflows/main.yml/badge.svg)

### Project Description :
- Easy Access Patient record is a system which is aimed at enabling the Medical Center to keep track of all the patients records and access them with ease. The developed system is helpful for management, patient health and research. In management, it could be used by the hospital’s director to see the performance of the physician, or statistical reporting.
- The physician can have the patient's history in detail from his previous records in less time. The physician can do their research by using advanced search. Archiving and securing electronic records is considered more reliable and trusted than paper-based records.

### Features

- Build a web application that provides a simplified pleasing user experience and designed using state of the art microservices API architecture.
- It offers an easy to use interface for creating and maintaining Patient Records and Prescriptions for each of the registered patients.
- The main goal of this website is to facilitate patients access to their medical records and give them e-prescription on basis of past illness and current symptoms.

### Solutions:
To reduce the amount of time required for paper-work, we designed an EAPR system so that doctors are able to see the list of patients and are able to generate the E-prescription for the patient.The patients can view their prescriptions.

Doctors can store past history illness data, allergy intolerance data, problem/diagnosis data, prescription data with dose direction and order details

### Install and Run code 

1. Create database `eapr` in postgresql
`CREATE DATABASE eapr;`

2. Create a virtual environment: 
`python3 -m venv eapr`

3. Activate environment:
`source eapr/bin/activate`

4. Install the dependancies:
`pip install -r requirements.txt`

5. export JWT token `export JWT_SECRET_KEY="<your_key>"`
 
6. Run the code `python3 app.py`

7. Clean up `deactivate`

### Run locally with docker

Use docker-compose<br>
`docker-compose up --build`

### Test Code:
UI:<br>
`py.test --html=report.html -s`

Routes:<br>
`python3 -m pytest`

### Migrate DB
1. After changes in the models.py / DB, run the command:<br>
`flask db migrate -m "some message"`
2. Update the head to point to latest version of db <br>`flask db stamp head`
3. To sync changes run: <br>
`flask db upgrade`


## Tech stack
<strong>EAPR</strong> uses

<strong>Frontend</strong>:
1. HTML, CSS, JS
2. Bootstrap
3. Jinja Templating Language

<strong>Backend</strong>:
1. Flask
2. SQLAlchemy

<strong>Database:</strong>
PostgreSQL

<strong>Testing:</strong>
1. Selenium
2. PyTest

## Flow Diagram:
![Untitled Diagram drawio](https://user-images.githubusercontent.com/51478897/150688432-604952be-ba2e-412d-a562-02b43475d3f4.png)


## Database Schema:
![EAPR-DB](https://user-images.githubusercontent.com/51478897/149629535-9535a0f2-c268-4336-ab73-61b0cc45b9cb.png)


## Contributors:
[Forks](https://github.com/Bhanu9650/OpenEHR-Project/network/members)


- [Bhanu Gupta (I-1564)](https://github.com/Bhanu9650/OpenEHR-Project/commits?author=Bhanu9650) <br>
- [Dinesh Kumar (I-1563)](https://github.com/Bhanu9650/OpenEHR-Project/commits?author=dk-dinesh) <br>
- [Prabhpreet Singh (I-1555)](https://github.com/Bhanu9650/OpenEHR-Project/commits?author=prabhpreet332) <br>
- [Rohit Kashyap (I-1557)](https://github.com/Bhanu9650/OpenEHR-Project/commits?author=Rohit2998) <br>
- [Simran Gera (I-1554)](https://github.com/Bhanu9650/OpenEHR-Project/commits?author=simran-gera) <br>
- [Shruti Gupta (I-1553)](https://github.com/Bhanu9650/OpenEHR-Project/commits?author=shruti-17) <br>
- [Vinay Chauhan (I-1562)](https://github.com/Bhanu9650/OpenEHR-Project/commits?author=VinayPep) <br>


