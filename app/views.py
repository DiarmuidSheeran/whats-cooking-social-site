from django.shortcuts import render

# Create your views here.
@unauthenticated_user
def landing(request):
    return render(request, 'landing.html')