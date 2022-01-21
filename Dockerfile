FROM python:3.8.10
WORKDIR /OpenEHR-Project
ADD . /OpenEHR-Project
RUN pip install -r requirements.txt
CMD ["python","app.py"]