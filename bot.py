import requests
import os
from datetime import datetime

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

if not API_TOKEN or not CHAT_ID:
    raise ValueError("API Token or Chat ID is missing in environment variables.")


URL = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage'

# Get the current hour in 24-hour format
current_hour = datetime.now().hour

# The message to send
message = "Bong " * current_hour

# Send the message to the Telegram chat
payload = {
    'chat_id': CHAT_ID,
    'text': message.strip()  # Strip the trailing space
}

response = requests.post(URL, data=payload)

# Check for a successful response
if response.status_code == 200:
    print(f"Message sent successfully: {message}")
else:
    print(f"Failed to send message. Status code: {response.status_code}")
