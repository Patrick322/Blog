import urllib.request,json

quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_quote():
    with urllib.request.urlopen(quotes_url) as url:
        quotes_raw_data = url.read()
        quotes_response = json.loads(quotes_raw_data)
    return quotes_response