import yagmail
import os
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env file
load_dotenv()


sender = 'tekworld10@gmail.com'
file = pd.read_csv('contacts1.csv')


password = os.getenv("PASSWORD") # Secret password stored in .env file
mail = yagmail.SMTP(user=sender, password=password)

# This function generates file
def generate_file(filename, content):
  with open(filename, 'w') as f:
    f.write(str(content))

for index, row in file.iterrows():
  name = row['name']
  filename = name + ".txt"
  amount = row['amount']
  receiver = row['email']
  
  generate_file(filename, amount)
  subject = "Thi is the subject!"
  contents = [f"""
              Hi, {name} your charges is {amount}
              Bill attached!""", filename]
  
  mail.send(to=receiver, subject=subject, contents=contents)
  print('Email sent!')
  