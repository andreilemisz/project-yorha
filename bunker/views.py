from django.shortcuts import render

def startingpage(request):
    return render(request, 'bunker/homepage.html')
# Create your views here.
