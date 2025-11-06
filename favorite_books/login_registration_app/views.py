from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if request.method == 'POST':
        if len(errors) > 0 :
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:    
            user = User.objects.filter(email=request.POST['email']).first()
            if user:
                if bcrypt.checkpw(request.POST['password'].encode(),user.password.encode()):
                    request.session['user_id'] = user.id
                    messages.success(request,'successfully Logged in')
                    return redirect('book:main')
    return redirect('/')

def success(request):
    user_id = request.session['user_id']
    logged_user = User.objects.get(id=user_id)
    context = {
        'user_logged' : logged_user
    }
    return render(request,'success.html',context)

def register(request):
    if request.method == 'POST':
        errors = User.objects.userValidator(request.POST)
        if len(errors) > 0 :
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            password = request.POST.get('password')
            hashedPassword = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
            user= User.objects.create(first_name = request.POST.get('first_name'),
                            last_name = request.POST.get('last_name'),
                            birth_date = request.POST.get('birth_date'),
                            email = request.POST.get('email'),
                            password = hashedPassword)
        request.session['user_id'] = user.id
        messages.success(request,'successfully Logged in')
        return redirect('book:main')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

