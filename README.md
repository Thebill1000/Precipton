##Precipton

The Medication Reminder System is a web-based application designed to help healthcare professionals, such as pharmacists and doctors, manage patient medication schedules effectively. This system allows healthcare providers to input patient information, schedule medication reminders, and collect daily feedback from patients.

## Features

- **Patient Information Management:** Pharmacists and doctors can add patient names and prescribed medications to the system.
  
- **Flexible Reminders:** Reminders can be scheduled at intervals of 1 minute, 5 minutes, 30 minutes, or 1 hour before the medication time.
  
- **SMS and Email Notifications:** Automated SMS notifications using Twilio and email reminders using SendGrid are sent to patients based on the scheduled reminders.
  
- **Patient Feedback:** Patients can provide daily feedback on their well-being, allowing healthcare providers to monitor their condition.

## Installation

1. Clone the repository: `git clone https://github.com/yourusername/medication-reminder-system.git`
2. Navigate to the project directory: `cd medication-reminder-system`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On macOS/Linux: `source venv/bin/activate`
   - On Windows: `venv\Scripts\activate`
5. Install dependencies: `pip install -r requirements.txt`

## Configuration

1. Set up Twilio:
   - Create a Twilio account and obtain your Account SID, Auth Token, and Twilio phone number.
   - Replace `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER` placeholders in `app.py` with your Twilio credentials.

2. Set up SendGrid:
   - Create a SendGrid account and obtain your API Key.
   - Replace `SENDGRID_API_KEY` placeholder in `app.py` with your SendGrid API Key.

## Usage

1. Run the Flask application: `flask run`
2. Access the application in your web browser at `http://localhost:5000`
3. Input patient information, schedule reminders, and collect patient feedback using the web interface.

## Contributing

Contributions are welcome! Fork the repository and create a new branch for your feature or bug fix. After making changes, submit a pull request detailing your modifications.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to modify and expand upon this README to suit your project's specific needs. Good luck with your Medication Reminder System!
