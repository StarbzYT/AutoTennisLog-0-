# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from auth import *
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect

class Messages:
    def __init__(self, account_sid, auth_token):
        # Find your Account SID and Auth Token at twilio.com/console
        self.account_sid = account_sid
        self.auth_token = auth_token
    
    def message_history(self):
        client = Client(self.account_sid, self.auth_token)
        # message history
        messages = client.messages.list(limit=2)
        history = [message.body for message in messages]
        return history

message_history = Messages(account_sid, auth_token)
print(message_history.message_history())

# app = Flask(__name__)

# @app.route("/sms", methods=['GET', 'POST'])
# def sms_reply():
#     """Respond to incoming calls with a simple text message."""
#     # Start our TwiML response
#     resp = MessagingResponse()

#     # Add a message
#     resp.message("The Robots are coming! Head for the hills!")

#     return str(resp)

# if __name__ == "__main__":
#     app.run(debug=True)

# # Find your Account SID and Auth Token at twilio.com/console
# account_sid = account_sid
# auth_token = auth_token
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#                               body='Hi there',
#                               from_=trial_number,
#                               to=to_phone
#                           )

# print(message.sid)