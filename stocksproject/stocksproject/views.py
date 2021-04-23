from django.shortcuts import render

def stocks_view(request):
    # create a dictionary to pass
    # data to the template
    # return response with template and context
    return render(request, "index.html")
