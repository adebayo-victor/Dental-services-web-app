import os
from dotenv import load_dotenv
#loading stuff from dotenv
load_dotenv()
#get stuff from .env
POSTMAIL_URL = "https://postmail.invotes.com/send"
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
#mail function
import requests
def send_email(to_email, subject, message_body, reply_to="adebayooluseyi2@gmail.com"):
    payload = {
        "access_token": ACCESS_TOKEN,
        "subject": subject,
        "text": message_body,
        "reply_to": reply_to,
        "recipient": to_email
    }

    try:
        response = requests.post(POSTMAIL_URL, data=payload)
        print("✅ Status Code:", response.status_code)
        print("📨 Response:", response.text)
        return response.status_code == 200
    except Exception as e:
        print("❌ Error:", str(e))
        return False
send_email(
    to_email="adebayovictorvicade@gmail.com",
    subject="TECHLITE INNOVATIONS",
    message_body=f"Hello there, This is your  password => PLAy,🔐 try not to forget it"
)