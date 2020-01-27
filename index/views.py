from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    cards = Card.objects.all()
    return render(request, 'index/index.html', context={'cards': cards})