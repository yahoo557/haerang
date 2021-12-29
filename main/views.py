from django.shortcuts import render
from .models import Address

# Create your views here.
def main (request):
    addresses = Address.objects
    return render(request, 'index.html', {'addresses' : addresses})