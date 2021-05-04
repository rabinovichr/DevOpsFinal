import os
# import dotenv
from django.shortcuts import render
import finnhub

def stocks_view(request):
    load_dotenv()
    api_key = os.getenv('API_KEY')

    finnhub_client = finnhub.Client(api_key=api_key)

    aapl = finnhub_client.quote('AAPL')['c']
    tsla = finnhub_client.quote('TSLA')['c']
    amzn = finnhub_client.quote('AMZN')['c']
    gme = finnhub_client.quote('GME')['c']
    msft = finnhub_client.quote('MSFT')['c']
    sbux = finnhub_client.quote('SBUX')['c']
    amc = finnhub_client.quote('AMC')['c']
    nflx = finnhub_client.quote('NFLX')['c']
    ba = finnhub_client.quote('BA')['c']
    prty = finnhub_client.quote('PRTY')['c']

    return render(request, "index.html", {
        'aapl': aapl,
        'tsla': tsla, 
        'amzn': amzn, 
        'gme': gme, 
        'msft': msft,
        'sbux': sbux, 
        'amc': amc, 
        'nflx': nflx, 
        'ba': ba, 
        'prty': prty
        })
