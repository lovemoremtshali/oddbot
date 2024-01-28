from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import os
from twilio.rest import Client
import time
app = Flask(__name__)

TWILIO_ACCOUNT_SID = "AC2be1859052140e8b68cef69d8581602f"
TWILIO_AUTH_TOKEN = "9355ef407da6bca5659ce6bb3612a06c"

account_sid = 'AC9462301cf5262d799a3928a9c65986bc'
auth_token = '44dc8fce7b7de18d8d8ba9db4264d827'
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

'''

@app.route('/bot', methods=['POST'])
def handle_whatsapp_message():
    incoming_message = request.values.get('Body', '').lower()
    print(request.values.get('MediaUrl0'))
    media_url = request.values.get('MediaUrl0')
    #Client.requests.get(media_url)
    
        # Retrieve code snippet from Twilio media
        #code_media_sid = 'ME967f5a95a5f80f08d260ca35aef3b456'  # Replace with the actual SID
        #code_media = client.messages.media(code_media_sid).fetch()
        #code_content = code_media.uri
    #time.sleep(10.0)
    print('/n 1/n')
    code_content = client.messages(media_url.split('/')[4]).fetch()
    print('/n 2/n')

    response_message = f"Here's the code:\n{code_content}"
  

    resp = MessagingResponse()
    resp.message(response_message)
    return str(resp)

'''

@app.route('/bot', methods=['POST'])

def bot():
    incoming_message = request.values.get('Body', '').lower()
    media_url = request.values.get('MediaUrl0')  # Check for the first media URL
    resp = MessagingResponse()
    msg = resp.message()

    if media_url:
        # Download the file from Twilio's server to your server
        file_response = requests.get(media_url)
        file_name = media_url.split('/')[-1]  # Extract file name from URL

        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, file_name)
        with open(file_path, 'wb') as f:
            f.write(file_response.content)

        response_message = f"File '{file_name}' saved successfully!"
        image_file_path = os.path.join(os.path.dirname(__file__), 'ME8a4b96eb9ceef1b898f5f871841e96af')
        msg.body(response_message)
        msg.media(image_file_path)
    else:
        response_message = "Please send a file to store it on the server."

    
    #resp.message(response_message)
    
    return str(resp)




'''
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)

'''





if __name__ == '__main__':
    app.run(port=4000, debug=True)