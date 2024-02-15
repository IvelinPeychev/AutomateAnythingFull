from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text

    # Parse the html to the soup
    soup = BeautifulSoup(content, 'html.parser')

    # Find and manipulate the result
    result = soup.find('span',class_='ccOutputRslt').get_text()
    rate = float(result[:-4])

    return rate


currency_rate = get_currency('INR', 'USD')
print(currency_rate)

