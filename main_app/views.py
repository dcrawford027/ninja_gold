from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'purse' not in request.session:
        request.session['purse'] = 0
    if 'logs' not in request.session:
        request.session['logs'] = []
    return render(request, 'index.html')

def processMoney(request):
    loc = request.POST['location']
    if loc == 'farm':
        gold = random.randint(10, 20)
        request.session['purse'] += gold
        request.session['logs'].append('\nEarned ' + str(gold) + ' gold from the ' + loc + '!')
    elif loc == 'cave':
        gold = random.randint(5, 10)
        request.session['purse'] += gold
        request.session['logs'].append('\nEarned ' + str(gold) + ' gold from the ' + loc + '!')
    elif loc == 'house':
        gold = random.randint(2, 5)
        request.session['purse'] += gold
        request.session['logs'].append('\nEarned ' + str(gold) + ' gold from the ' + loc + '!')
    elif loc == 'casino':
        giveOrTake = random.randint(0, 10) % 2
        if giveOrTake == 0:
            gold = random.randint(0, 50)
            request.session['purse'] += gold
            request.session['logs'].append('\nEntered a casino and won ' + str(gold) + ' gold! Lucky!')
        elif giveOrTake == 1:
            gold = random.randint(0, 50)
            request.session['purse'] -= gold
            request.session['logs'].append('\nEntered a casino and lost ' + str(gold) + ' gold... Ouch..')
    return redirect('/')

def clearSession(request):
    del request.session['purse']
    del request.session['logs']
    return redirect('/')