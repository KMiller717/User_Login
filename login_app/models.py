from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

    
        if len(post_data['first_name']) < 2 or len(post_data['first_name']) > 56: 
            errors['first_name'] = 'First name needs to be more than 2 characters'
        
        if len(post_data['last_name']) < 2 or len(post_data['last_name']) >56:
            errors['last_name'] = 'Last name needs to be more than 2 characters'
        
        try:
            User.objects.get(email = post_data['email'])
            errors['email'] = 'Email address already in use'
        except:
            pass 
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"       
        
        if len(post_data['password']) <8:
            errors['password'] ='Password must be at least eight characters long'
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = 'Passwords do not match'
            
        return errors
    


class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField (max_length=55)
    email = models.CharField(max_length=55)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

