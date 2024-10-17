import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


sender = 'tekworld10@gmail.com'
receiver = 'nuel6700@gmail.com'
password = "enterYourOutlookHotmailPasswd"

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Testing Email Automation!'

body = """
<h1>Hello and Welcome!<h1>
This is a simple email to test run
for Testing Email Automation
"""
mimetext = MIMEText(body, 'html')
message.attach(mimetext)

attachment_path = 'lp1.jpg'
attachment_file = open(attachment_path, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload(attachment_file.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disosition', 'attachment', filename=attachment_path)
message.attach(payload)

server = smtplib.SMTP('smpt.office365.com', 587)
server.starttls()
server.login(sender, password)
message_text = message.as_string()
print(message_text)
server.sendmail(sender, receiver, message_text)
server.quit()