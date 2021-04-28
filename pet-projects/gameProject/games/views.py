from django.shortcuts import render

# Create your views here.
def guessnumber(request):
    return render(request, 'games/guessnumber.html')
