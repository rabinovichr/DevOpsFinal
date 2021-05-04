import os
import dotenv
from django.shortcuts import render
import finnhub

def stocks_view(request):
    # create a dictionary to pass
    # data to the template
    # return response with template and context
    dotenv.load_dotenv()
    api_key = os.getenv('API_KEY')

    finnhub_client = finnhub.Client(api_key=api_key)
    aapl = finnhub_client.quote('AAPL')
    context = {'aapl': aapl}
    return render(request, "index.html", context)
