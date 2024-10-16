# This script sends email with attachments
import yagmail
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

sender = 'tekworld10@gmail.com'
receiver = 'vyhew0sob0d3@10mail.xyz'

subject = "This is the subject"

# Converted to a list
contents = ["""
Hi,
I am testing emails automation
""", 'text.txt']

# Get the password from the environment variable
password = os.getenv('PASSWORD')

yag = yagmail.SMTP(user=sender, password=password)
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")
