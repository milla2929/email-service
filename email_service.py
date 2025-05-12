from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests (required for ESP32)

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "million292929@gmail.com"  # Replace with your email
SENDER_PASSWORD = "subg qqlc aqxt fjaf"  # Replace with your email password

# Email endpoint
@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        # Get the JSON payload from the POST request
        data = request.json
        subject = data.get('subject', 'AFib Alert')
        message = data.get('message', 'Atrial Fibrillation has been detected. Immediate action is required.')
        recipient_email = data.get('recipient_email', 'million292929292929@gmail.com')  # Replace with recipient email

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()

        print("Email sent successfully!")
        return jsonify({'success': True, 'message': 'Email sent successfully!'}), 200

    except Exception as e:
        print("Error:", str(e))
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == 'main':
    app.run(debug=True, port=5000)