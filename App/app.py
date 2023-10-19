#!/usr/bin/python3
from flask import Flask, request, jsonify
from twilio.rest import Client
import mandrill
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
db = SQLAlchemy(app)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    medication = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), nullable=False)

db.create_all()

# Twilio credentials
TWILIO_ACCOUNT_SID = 'ACb78b0fd70d33ac6cabf5308a70f73c2f'
TWILIO_AUTH_TOKEN = '5a121b6623138bf8b9da439ad61e261d'
TWILIO_PHONE_NUMBER = '+2347063808082'

# Mandrill API key
MANDRILL_API_KEY = 'md-ae8bYGk7lI679BT04SfNJQ'

# ... (other routes)

@app.route('/add_patient', methods=['POST'])
def add_patient():
    data = request.get_json()
    name = data['name']
    medication = data['medication']
    phone_number = data['phone_number']
    email = data['email']

    new_patient = Patient(name=name, medication=medication, phone_number=phone_number, email=email)
    db.session.add(new_patient)
    db.session.commit()

    return jsonify({'message': f'Patient {name} added successfully!'}), 201

# ... (other routes)

