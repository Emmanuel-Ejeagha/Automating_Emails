# Send multiples emails to different contacts
import yagmail
import os
import pandas
from dotenv import load_dotenv


load_dotenv()
sender = 'tekworld10@gmail.com'
password = os.getenv("PASSWORD") # Secret password stored in .env file
mail = yagmail.SMTP(user=sender, password=password)

file = pandas.read_csv('contacts1.csv')

for index, row in file.iterrows():
  receiver = row['email']
  subject = "This is the subject"
  contents = [f"""
             Hi, {row['name']} your bill is {row['amount']}
             Below is your invoice""",
             row['filepath'],
             ]
  mail.send(to=row['email'], subject=subject, contents=contents)
  print("Email Sent!")