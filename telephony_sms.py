# src/telephony_sms.py
# pip install twilio

from twilio.rest import Client

# Twilio credentials (replace with your actual credentials)
account_sid = "your_account_sid"
auth_token = "your_auth_token"
twilio_number = "your_twilio_number"
client = Client(account_sid, auth_token)

# Function to send an SMS
def send_sms(to_number, message):
    message = client.messages.create(
        body=message,
        from_=twilio_number,
        to=to_number
    )
    return message.sid

# Function to make a phone call
def make_call(to_number, from_number, url):
    call = client.calls.create(
        to=to_number,
        from_=from_number,
        url=url
    )
    return call.sid

# Function to handle incoming calls
def handle_incoming_call(call_sid):
    call = client.calls(call_sid).fetch()
    if call.status == "ringing":
        client.calls(call_sid).update(status="completed")
        return "Call answered"
    else:
        return "No incoming call"

# Test the telephony and SMS functions
if __name__ == "__main__":
    to_number = "+1234567890"
    message = "Hello, this is a test message."
    sms_sid = send_sms(to_number, message)
    print(f"SMS sent with SID: {sms_sid}")

    call_sid = make_call(to_number, twilio_number, "http://demo.twilio.com/docs/voice.xml")
    print(f"Call initiated with SID: {call_sid}")

    call_status = handle_incoming_call(call_sid)
    print(f"Call status: {call_status}")
