import requests
import os
import pytz
from datetime import datetime

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

if not API_TOKEN or not CHAT_ID:
    raise ValueError("API Token or Chat ID is missing in environment variables.")


URL = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage'

timezone = pytz.timezone('Etc/GMT-3')  # GMT+3 is represented as GMT-3 in pytz
current_time = datetime.now(timezone)

# Get the current hour in 12-hour format
current_hour = current_time.strftime('%I')  # %I gives 12-hour format without leading zero
current_hour = int(current_hour)  # Convert to integer to use in message construction

# The message to send
message = "BONG " * current_hour

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
