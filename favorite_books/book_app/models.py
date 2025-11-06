from django.db import models

# Create your models here.
from login_registration_app.models import User
# class User(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#   # liked_books = a list of books a given user likes
#   # books_uploaded = a list of books uploaded by a given user   
class BookManager(models.Manager):
    
    def bookValidator(self, postData):
        err={}
        title = postData.get('title')
        desc  = postData.get('desc')
        if not title:
            err['title_required'] = 'Please enter the title.'
        if len(desc) < 5:
            err['description_length'] = 'Description must be at least 5 characters.' 
        return err           


# class usser :
#     list of liked_books
#     list of books_uploaded 


class Book(models.Model):
    title = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, related_name = "books_uploaded", on_delete = models.CASCADE) 
    users_who_like = models.ManyToManyField(User, related_name = "liked_books") 
    desc=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()