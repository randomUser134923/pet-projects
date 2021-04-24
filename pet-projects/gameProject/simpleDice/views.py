from django.shortcuts import render

# Create your views here.
    

def index(request):
    return render(request, 'simpleDice/index.html')
    
def diceview(request):
    return render(request,'simpleDice/dice.html')