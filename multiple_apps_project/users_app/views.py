from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welecome to Home Page.")

def register(request):
    return HttpResponse("placeholder for users to create a new user record.")

def login(request):
    return HttpResponse("placeholder for users to log in.")

def show(request):
    return HttpResponse("placeholder to display all the list of users later.")