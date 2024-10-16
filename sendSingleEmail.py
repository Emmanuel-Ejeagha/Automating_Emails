import yagmail
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

sender = 'tekworld10@gmail.com'
receiver = 'nuel6700@gmail.com'

subject = "This is the subject"

contents = """
Hi,
I am testing automating emails
"""

# Get the password from the environment variable
password = os.getenv('PASSWORD')

yag = yagmail.SMTP(user=sender, password=password)
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent")
