import requests

url = 'https://api.languagetool.org/v2/check'

data = {
    'text': 'Tis is a nixe day!',
    'language': 'auto'
}

response = requests.post(url, data=data).json()

print(response)
