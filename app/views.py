from django.shortcuts import render
from .models import *
from .decorators import unauthenticated_user

# Create your views here.
@unauthenticated_user
def landing(request):
    return render(request, 'landing.html')