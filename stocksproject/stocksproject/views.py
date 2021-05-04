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
    context = {'aapl': aapl}
    return render(request, "index.html", context)

    finnhub_client = finnhub.Client(api_key=api_key)
    aapl = finnhub_client.quote('TSLA')
    context = {'tsla': aapl}
    return render(request, "index.html", context)

    finnhub_client = finnhub.Client(api_key=api_key)
    aapl = finnhub_client.quote('AMZN')
    context = {'amzn': aapl}
    return render(request, "index.html", context)

    finnhub_client = finnhub.Client(api_key=api_key)
    aapl = finnhub_client.quote('GME')
    context = {'gme': aapl}
    return render(request, "index.html", context)

    finnhub_client = finnhub.Client(api_key=api_key)
    aapl = finnhub_client.quote('MSFT')
    context = {'msft': aapl}
    return render(request, "index.html", context)

    finnhub_client = finnhub.Client(api_key=api_key)
    aapl = finnhub_client.quote('SBUX')
    context = {'sbux': aapl}
    return render(request, "index.html", context)

    finnhub_client = finnhub.Client(api_key=api_key)
    aapl = finnhub_client.quote('AMC')
    context = {'amc': aapl}
    return render(request, "index.html", context)

    finnhub_client = finnhub.Client(api_key=api_key)
    aapl = finnhub_client.quote('NFLX')
    context = {'nflx': aapl}
    return render(request, "index.html", context)

    finnhub_client = finnhub.Client(api_key=api_key)
    aapl = finnhub_client.quote('BA')
    context = {'ba': aapl}
    return render(request, "index.html", context)

    finnhub_client = finnhub.Client(api_key=api_key)
    aapl = finnhub_client.quote('PRTY')
    context = {'prty': aapl}
    return render(request, "index.html", context)
