from flask import Flask, Blueprint, jsonify
import datetime
from twilio.rest import Client
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from handle_upload import handle_upload
# Use the variable with:
import os

load_dotenv()

# TODO: schedule this daily at a certain time. 
# TODO: look if I can automatically upload a note from my phone using shortcuts


twilio_account = os.getenv("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone_no = os.getenv("TWILIO_PHONE_NUMBER")
recipient_phone_no = os.getenv("RECIPIENT_PHONE_NUMBER")
db_password = os.getenv("DB_PASSWORD")
db_username = os.getenv("DB_USERNAME")

app = Flask(__name__)
app.register_blueprint(handle_upload)

# TODO: so here we need to setup the database.
# we want to define the database first
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_username}:{db_password}@localhost:5432/notes_db'
db = SQLAlchemy(app)

# Twilio account information
# account_sid = twilio_account
# auth_token = twilio_auth
client = Client(twilio_account, twilio_auth_token)

# TODO: come back and fix this

@app.route("/send_reminder")
def send_reminder():
    # Get the current time
    now = datetime.datetime.now()
    # Set the reminder message
    message = "Don't forget to do something today!"
    # Send the message via SMS
    message = client.messages.create(   
        to=recipient_phone_no, 
        from_=twilio_phone_no,
        body=message)
    return "Reminder sent!"


@app.route('/fetch_notes', methods=["GET"])
def fetch_notes():
    from db import Note
    notes = Note.query.all()
    return jsonify([note.to_dict() for note in notes])
    

