import requests

# r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2024-1-27&to=2024-1-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
#
# content = r.json()
#


def get_news(topic, from_date, to_date, language='en', apiKey='6e126fadbd2540b2a2b7971d78823980'):
    url = (f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}'
           f'&sortBy=popularity&language=en&apiKey={apiKey}')

    r = requests.get(url)
    content = r.json()

    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"Title\n {article['title']}, '\nDescription\n' {article['description']}")

    return results

print(get_news('space','2024-1-27', '2024-1-28'))
