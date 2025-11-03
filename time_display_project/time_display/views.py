from django.shortcuts import render
from time import strftime, localtime

def index(request):
    context = {
        "date": strftime("%b %d %Y", localtime()),   # Oct 26 2013
        "time": strftime("%I:%M %p", localtime())    # 11:26 AM
    }
    return render(request, 'index.html', context)
