from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
def main(request):
    id=request.session['user_id']
    user=User.objects.get(id=id)
    context={
      "logged_user":user,
      "all_books":Book.objects.all(),
    }
    return render(request,"main.html",context)

def add_book(request):
    errors=Book.objects.bookValidator(request.POST)
    if request.method == 'POST':
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
                return redirect('book:main')
        else:
            user =User.objects.get(id=request.session['user_id'])
            fav_book= Book.objects.create(title=request.POST['title'],desc=request.POST['desc'],uploaded_by=user)
            fav_book.users_who_like.add(user)
            return redirect('book:main')
        
def add_favorite(request,book_id):
    user =User.objects.get(id=request.session['user_id'])
    fav_book=Book.objects.get(id=book_id) 
    fav_book.users_who_like.add(user)
    print(f"{book_id}")
    return redirect('book:main') 

def un_favorite(request,book_id):
    user =User.objects.get(id=request.session['user_id'])
    fav_book=Book.objects.get(id=book_id) 
    fav_book.users_who_like.remove(user)
    print(f"{book_id}")
    return redirect('book:main')

     
def edit_book(request,book_id):
    id=request.session['user_id']
    user=User.objects.get(id=id)
    book=Book.objects.get(id=book_id)
    context={
      "logged_user":user,
      "liked_user": book.users_who_like.all(),
      "book" :book
    }    
    return render(request,"edit_book.html",context) 
        
           
def view_book(request,book_id):
    id=request.session['user_id']
    user=User.objects.get(id=id)
    book=Book.objects.get(id=book_id)
    context={
      "logged_user":user,
      "book" :book,
      "liked_user":book.users_who_like.all()
    } 
    
    return render(request,"view_book.html",context) 

def delete_book(request,book_id):
        id=request.session['user_id']
        user=User.objects.get(id=id)
        book=Book.objects.get(id=book_id)
        book.delete()
        messages.success(request, "Delete Book successfully!")
        return redirect('book:main')

def update_book(request,book_id):
    if request.method == 'POST':
        id=request.session['user_id']
        user=User.objects.get(id=id)
        book=Book.objects.get(id=book_id)
        book.title = request.POST['title']
        book.desc = request.POST['desc']
        book.save()
        messages.success(request, "Book updated successfully!")
    return redirect('book:edit_book',book_id=book_id) 
 
