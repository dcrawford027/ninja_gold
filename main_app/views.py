from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'purse' not in request.session:
        request.session['purse'] = 0
    if 'log' not in request.session:
        request.session['log'] = []
    return render(request, 'index.html')

def processMoney(request):
    loc = request.POST['location']
    if loc == 'farm':
        request.session['purse'] += random.randint(10, 20)
    elif loc == 'cave':
        request.session['purse'] += random.randint(5, 10)
    elif loc == 'house':
        request.session['purse'] += random.randint(2, 5)
    elif loc == 'casino':
        giveOrTake = random.randint(0, 10) % 2
        if giveOrTake == 0:
            request.session['purse'] += random.randint(0, 50)
        elif giveOrTake == 1:
            request.session['purse'] -= random.randint(0, 50)
    return redirect('/')