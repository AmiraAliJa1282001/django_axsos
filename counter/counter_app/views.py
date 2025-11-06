from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

def index(request):
    # لو ما في "counter" في الـ session، أنشئيه
    if 'counter' not in request.session:
        request.session['counter'] = 0


    request.session['counter'] += 1

    if 'visits' not in request.session:
        request.session['visits'] = 1
    else:
        request.session['visits'] += 1

    context = {
        "counter": request.session['counter'],
        "visits": request.session['visits'],
    }
    return render(request, "index.html", context)


def destroy(request):

    request.session.flush()
    return redirect('/')


def plus_two(request):
   
    request.session['counter'] += 2
    return redirect('/')


def custom_increment(request):
  
    if request.method == "POST":
        increment = int(request.POST.get('increment', 1))
        request.session['counter'] += increment
    return redirect('/')
