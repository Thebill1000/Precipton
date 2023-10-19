from flask import Flask, request, render_template
from twilio.rest import Client

app = Flask(__name__)

# Twilio credentials
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'

client = Client(account_sid, auth_token)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule', methods=['POST'])
def schedule_reminder():
    patient_name = request.form['patient_name']
    medication_name = request.form['medication_name']
    phone_number = request.form['phone_number']
    reminder_time = request.form['reminder_time']

    # Schedule reminders using Twilio
    reminder_message = f"Hello {patient_name}! Don't forget to take your {medication_name}."

    # Convert reminder time to seconds
    if reminder_time == '1':
        reminder_seconds = 60
    elif reminder_time == '5':
        reminder_seconds = 300
    elif reminder_time == '30':
        reminder_seconds = 1800
    else:
        reminder_seconds = 3600

    # Schedule SMS reminder
    message = client.messages.create(
        to=phone_number,
        from_=twilio_phone_number,
        body=reminder_message,
        send_at=int(time.time()) + reminder_seconds
    )

    return f"Reminder scheduled successfully! Message SID: {message.sid}"

if __name__ == '__main__':
    app.run(debug=True)

