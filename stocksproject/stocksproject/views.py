import os
from dotenv import load_dotenv
from django.shortcuts import render
import finnhub

def stocks_view(request):
    # create a dictionary to pass
    # data to the template
    # return response with template and context
    load_dotenv()
    api_key = os.getenv('c1s391aad3i8lrmfh4o0')

    finnhub_client = finnhub.Client(api_key=api_key)

    aapl = finnhub_client.quote('AAPL')



    tsla = finnhub_client.quote('TSLA')



    amzn = finnhub_client.quote('AMZN')



    gme = finnhub_client.quote('GME')



    msft = finnhub_client.quote('MSFT')


    sbux = finnhub_client.quote('SBUX')



    amc = finnhub_client.quote('AMC')


    nflx = finnhub_client.quote('NFLX')



    ba = finnhub_client.quote('BA')
    


    prty = finnhub_client.quote('PRTY')

    return render(request, "index.html", {'aapl': aapl,'tsla': tsla, 'amzn': amzn, 'gme': gme, 'msft': msft,'sbux': sbux, 'amc': amc, 'nflx': nflx, 'ba': ba, 'prty': prty})
