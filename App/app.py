from flask import Flask, render_template, request
from twilio.rest import Client
import mandrill

app = Flask(__name__)

# Twilio and Mandrill configurations
TWILIO_ACCOUNT_SID = 'ACb78b0fd70d33ac6cabf5308a70f73c2f'
TWILIO_AUTH_TOKEN = 'e55bcd7ead88c6e8e756692f4a4389b7'
TWILIO_PHONE_NUMBER = '+15173250595'
MANDRILL_API_KEY = 'md-ae8bYGk7lI679BT04SfNJQ'

twilio_client = Client(ACb78b0fd70d33ac6cabf5308a70f73c2f, e55bcd7ead88c6e8e756692f4a4389b7)
mandrill_client = mandrill.Mandrill(md-ae8bYGk7lI679BT04SfNJQ)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    phone_or_email = request.form['phoneOrEmail']
    medication = request.form['medication']
    pills_count = request.form['pillsCount']
    medication_duration = request.form['medicationDuration']
    first_dose_time = request.form['firstDoseTime']
    reminder_interval = request.form['reminderInterval']

    # Save patient data to the database (you might want to add this part)

    # Send SMS notification
    sms_message = f"Hello {name}, it's time to take your medication: {medication}. Please take {pills_count} pills."
    send_sms(phone_or_email, sms_message)

    # Send email notification (if email is provided)
    if '@' in phone_or_email:
        email_subject = "Medication Reminder"
        email_message = f"Hello {name},\n\nIt's time to take your medication: {medication}.\n\nPlease take {pills_count} pills.\n\nBest regards,\nYour Healthcare Team"
        send_email(phone_or_email, email_subject, email_message)

    return "Notifications sent successfully!"

def send_sms(phone_number, message):
    twilio_client.messages.create(to=phone_number, from_=TWILIO_PHONE_NUMBER, body=message)

def send_email(recipient_email, subject, message):
    message_data = {
        'from_email': 'your_email@example.com',
        'to': [{'email': recipient_email}],
        'subject': subject,
        'text': message,
    }
    mandrill_client.messages.send(message=message_data, async=False)

if __name__ == '__main__':
    app.run(debug=True)

