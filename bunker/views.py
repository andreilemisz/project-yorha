from django.shortcuts import render

def bunker_startingpage(request):
    return render(request, 'bunker/homepage.html')
# Create your views here.
