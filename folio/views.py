from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
def PortView(request):
    return render(request, 'folio/index.html')
