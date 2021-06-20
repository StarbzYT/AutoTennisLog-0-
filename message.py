# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from auth import *

# Find your Account SID and Auth Token at twilio.com/console
account_sid = account_sid
auth_token = auth_token
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there',
                              from_=trial_number,
                              to=to_phone
                          )

print(message.sid)