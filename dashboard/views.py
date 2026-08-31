from django.shortcuts import render

...
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('dashboard.index_viewer', raise_exception=True)
def index(request):

    data = {
        'title': "Landing Page' Dashboard",
    }

    return render(request, 'dashboard/index.html', data)