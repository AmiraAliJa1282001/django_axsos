from django.db import models
import bcrypt
import re
from datetime import date, datetime

class UserManager(models.Manager):
    def userValidator(self, postData):
        first = postData.get('first_name')
        last  = postData.get('last_name')
        email = postData.get('email')
        pw    = postData.get('password')
        birth_raw = postData.get('birth_date')
        confirm = postData.get('confirm_pass')
        err = {}
        name_re = re.compile(r'^[A-Za-z]+$')
        email_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
 
        # First name
        if not first:
            err['first_name_required'] = 'Please enter first name.'
        elif len(first) < 2:
            err['first_name_length'] = 'First name must be at least 2 characters.'
        elif not name_re.fullmatch(first):
            err['first_name_format'] = 'First name must contain letters (and optional spaces/hyphens).'

        # Last name
        if not last:
            err['last_name_required'] = 'Please enter last name.'
        elif len(last) < 2:
            err['last_name_length'] = 'Last name must be at least 2 characters.'
        elif not name_re.fullmatch(last):
            err['last_name_format'] = 'Last name must contain letters (and optional spaces/hyphens).'

        # Email
        if not email:
            err['email_required'] = 'Please enter email.'
        elif not email_re.fullmatch(email):
            err['email_invalid'] = 'Please enter a valid email address.'
        elif User.objects.filter(email=email):
            err['email_taken'] = 'This email is already registered.'

        # Password
        if not pw:
            err['password_required'] = 'Please enter password.'
        elif len(pw) < 8:
            err['password_length'] = 'Password must be at least 8 characters.'
        elif pw != confirm:
            err['password_mismatch'] = 'Passwords do not match.'
        
        # birth_date
        if not birth_raw:
            err['birth_date_required'] = 'Please enter your birth date.'
        else:
            dob = datetime.strptime(birth_raw.strip(), "%Y-%m-%d").date()
            if dob:
                today = date.today()
                if dob > today:
                    err['birth_date_future'] = 'Birth date cannot be in the future.'
                else:
                    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                    if age < 13:
                        err['birth_date_age'] = 'You must be at least 13 years old to register.'


        return err

    def loginValidator(self,postDate):
        err ={}
        user =User.objects.filter(email=postDate['email']).first()
        if user :
            if not bcrypt.checkpw(postDate['password'].encode(),user.password.encode()):
                err['password_wrong']='This email or password is not regisetred'
        else:
           err['password_wrong']='This email or password is not regisetred'
        return err               
        
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254,unique=True)
    password = models.CharField(max_length=100)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

