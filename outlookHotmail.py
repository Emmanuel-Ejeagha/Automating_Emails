import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

sender = 'tekworld10@gmail.com'
receiver = 'nuel6700@gmail.com'
password = "enterYourOutlookHotmailPasswd"

message = """
Subject: Testing Email Automation

This is a simple email to test run
for Testing Email Automation

"""

server = smtplib.SMTP('smpt.office365.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()