from django.shortcuts import render

...
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    data = {
        'title': "Landing Page' Dashboard",
    }

    return render(request, 'dashboard/index.html', data)