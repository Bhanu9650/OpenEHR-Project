# Easy Access Patient Records

### Project Description :
- Easy Access Patient record is a system which is aimed at enabling the Medical Center to keep track of all the patients records and access them with ease. The developed system is helpful for management, patient health and research. In management, it could be used by the hospital’s director to see the performance of the physician, or statistical reporting.
- The physician can have the patient's history in detail from his previous records in less time. The physician can do their research by using advanced search. Archiving and securing electronic records is considered more reliable and trusted than paper-based records.

### Features

- Build a web application that provides a simplified pleasing user experience and designed using
state of the art microservices API architecture.
- It offers an easy to use interface for creating and maintaining Patient Records and Prescriptions for
each of the registered patients.
- The main goal of this website is to facilitate patients access to their medical records and give them
e-prescription on basis of past illness and current symptoms.

### Solutions:
To reduce the amount of time required for paper-work, we designed an EAPR system so that doctors are able to see the
list of patients and are able to generate the E-prescription for the patient.The patients can view their prescriptions.


Doctors can store past history illness data, allergy intolerance data, problem/diagnosis data,prescription data with dose
direction and order details

### Install and Run code 

1. Create database `eapr` in postgresql
`CREATE DATABASE eapr;`

2. Create a file `.config.json` and add the following values or the specific username and password, and add it in the project directory:
```json
    {
        "DB":
        {
            "DB_USER": "postgres",
            "DB_PWD": "password"
        }
    }
```
3. Create a virtual environment: 
`python3 -m venv eapr`

4. Activate environment:
`source eapr/bin/activate`

5. Install the dependancies:
`pip install -r requirements.txt`

6. export `JWT_SECRET_KEY="<your_key>"`

7. Run the code
`python3 app.py`

8. Clean up
`deactivate`

### Tech stack
<strong>EAPR</strong> uses

<strong>Frontend</strong>:
1. HTML/CSS
2. Bootstrap
3. Jinja Templating Language

<strong>Backend</strong>:
1. Flask
2. SQLAlchemy

<strong>Database:</strong>
PostgreSQL

<strong>Database Schema:</Strong>
![EAPR-DB](https://user-images.githubusercontent.com/51478897/149629535-9535a0f2-c268-4336-ab73-61b0cc45b9cb.png)


### Contributors:

- Bhanu Gupta (I-1564) <br>
- Dinesh Kumar (I-1563) <br>
- Prabhpreet Singh (I-1555) <br>
- Rohit Kashyap (I-1557) <br>
- Simran Gera (I-1554) <br>
- Shruti Gupta (I-1553) <br>
- Vinay Chauhan (I-1562) <br>

