from django.shortcuts import render, redirect

# Create your views here.
def index(request):
     return render(request, 'index.html')

def create(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['dojo_location'] = request.POST['dojo_location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST.get('comment', '')
        
        return redirect('/result')
    return redirect('/')

def result(request):
    context = {
        "name": request.session.get('name', ''),
        "dojo_location": request.session.get('dojo_location', ''),
        "language": request.session.get('language', ''),
        "comment": request.session.get('comment', ''),
        
    }
    return render(request, "result.html", context)