#  This script scraped an currency rate website
from bs4 import BeautifulSoup
import requests


def get_currency(from_curr, to_curr):
  url = f'https://www.x-rates.com/calculator/?from={from_curr}&to={to_curr}&amount=1'
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find('span', class_='ccOutputRslt').get_text()
  rate = float(rate[:-4])
  
  return rate

currency_rate = get_currency('EUR', 'AUD')
print(currency_rate)