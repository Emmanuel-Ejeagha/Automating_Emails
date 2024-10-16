import yagmail
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

sender = 'tekworld10@gmail.com'
subject = "This is the subject"

# Log in to Gmail
password = os.getenv('PASSWORD')
yag = yagmail.SMTP(user=sender, password=password)

# Importing contacts file
contacts = pd.read_csv('contacts.csv')

# Remove any leading/trailing spaces from the column headers
# contacts.columns = contacts.columns.str.strip()

for index, row in contacts.iterrows():
    # print(row['email'])
    contents = f"""
Hi {row['name']}
I am testing email automation using Python.
"""
    yag.send(to=row['email'], subject=subject, contents=contents)
    print("Emails Sent!")
