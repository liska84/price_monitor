import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
phone_number = os.environ['DESTINATION_PHONE_NUMBER']
twilio_number = os.environ['TWILIO_PHONE_NUMBER']

client = Client(account_sid, auth_token)

def sendSMS(price):
    message = client.messages.create(
                        body = f"The subscription price has been changed to {price}",
                        from_ = twilio_number,
                        to = phone_number,
                    )
    # print(message.sid)