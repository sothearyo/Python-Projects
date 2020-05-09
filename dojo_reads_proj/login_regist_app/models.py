from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        # errors for full name length
        if len(postData['full_name'])<2:
            errors["full_name"] = "First name should be at least 2 characters"
        if len(postData['full_name'])>100:
            errors["full_name"] = "First name should be less than 100 charcters"
        # errors for last alias
        if len(postData['alias'])<2:
            errors["alias"] = "Last name should be at least 2 characters"
        if len(postData['alias'])>100:
            errors["alias"] = "Last name should be less than 100 charcters"
        # error for valid email address
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        # error for duplicate email address
        emails = User.objects.filter(email=postData["email"])
        if len(emails) > 0:
            errors['email_duplicate'] = "That email already exists"
        # errors for password length
        if len(postData['password'])<8:
            errors["password"] = "Password should be at least 8 characters"
        if len(postData['password'])>45:
            errors["password"] = "Password should be less than 45 charcters"
        #error for confirm password
        if postData['password'] != postData['confirm_pw']:
            errors['confirm_pw'] = "Passwords do not match!"
        # return all errors    
        return errors

    def login_validator(self, postData):
        errors = {}
        # error for incorrect password
        try:
            user = User.objects.get(email=postData['email'])
            if user.password != postData['password']:
                errors["incorrect_pw"] = "Incorrect password"
        except:
            errors["email_login"] = "Email not found"
        # errors for valid email address
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email_login'] = "Please enter a valid email address"
        return errors
    


# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)
    objects = UserManager()

