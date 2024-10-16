import yagmail
import os
from dotenv import load_dotenv
import time
from datetime import datetime as dt


# Load environment variables from .env file
load_dotenv()

sender = 'tekworld10@gmail.com'
receiver = 'nuel6700@gmail.com'

subject = "This is the subject"

contents = """
Hi,
I am testing automating emails
"""

# Send email daily at 3pm
while True:
    now = dt.now()
    if now.hour == 15 and now.minute == 15:
        password = os.getenv('PASSWORD')
        yag = yagmail.SMTP(user=sender, password=password)
        yag.send(to=receiver, subject=subject, contents=contents)
        print("Email Sent!")
        time.sleep(3600)
