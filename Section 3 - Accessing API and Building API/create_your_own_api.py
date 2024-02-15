from flask import Flask, jsonify

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





app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Current Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
    rate = get_currency(in_cur, out_cur)
    result_dictionary = {'input_currency': in_cur, 'out_currency': out_cur, 'rate': rate}
    return jsonify(result_dictionary)

app.run()

