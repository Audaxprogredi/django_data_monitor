from django.shortcuts import render

...
from django.http import HttpResponse

def index(request):

    data = {
        'title': "Landing Page' Dashboard",
    }

    return render(request, 'dashboard/index.html', data)