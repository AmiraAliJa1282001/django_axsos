import random
from django.shortcuts import render,redirect

leaderboard = []
def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['message'] = None
        request.session['attempt'] = 0
        request.session['gameOver'] = False
        request.session['color'] = None  
        
    print(request.session['number']) 

    context = {
    'message': request.session.get('message'),
    'attempt': request.session.get('attempt'),
    'gameOver': request.session.get('gameOver'),
    'color': request.session.get('color'),
    }   
    return render(request,"index.html",context)  

def guess(request):
    if request.method == 'POST':
        if request.session.get('gameOver'):
            return redirect('index')

        guess_number = int(request.POST['guess'])
        number = request.session['number']
        request.session['attempt'] += 1

        if guess_number < number:
            request.session['message'] = "Too Low!"
            request.session['color'] = 'red'

        elif guess_number > number:
            request.session['message'] = "Too High!"
            request.session['color'] = 'red'

        else:
            request.session['message'] = f"Correct! The number was {number}"
            request.session['gameOver'] = True
            request.session['color'] = 'green'

        if request.session['attempt'] >= 5 and not request.session['gameOver']:
            request.session['message'] = f"You Lose! The number was {request.session['number']}."
            request.session['color'] = 'red'
            request.session['gameOver'] = True

    return redirect('/')


def reset(request):
    request.session.flush()
    return redirect('/')


def submit_name(request):
    if request.method == 'POST':
        winner_name = request.POST['name']
        leaderboard.append({"name": winner_name, "attempt": request.session['attempt']})
        return redirect('/leaderboard')


def leaderboard_view(request):
    return render(request, 'leaderboard.html', {'leaderboard':leaderboard})
         