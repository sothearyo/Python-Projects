from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class TVShowManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        # check that the show title is greater than 2 characters
        if len(postData['title']) < 2:
            errors['title_length'] = "Show title should be at least 2 characters"

        # check that the network is greater than 3 characters    
        if len(postData['network']) < 3:
            errors['network'] = "Show network should be at least 3 characters"

        # okay to have no description, but if there is, it must be greater than 10 characters    
        if len(postData['description']) > 1:
            if len(postData['description']) < 10:
                errors['description'] = "Description should be at least 10 characters" 

        # check that the release date is in the past           
        try:
            if datetime.strptime(postData['release_date'],'%Y-%m-%d') > datetime.now():
                errors['release_date'] = "Please enter a date in the past"
        except:
            errors['release_date'] = "Please enter a release date."      

        # return the errors dictionary    
        return errors  
         
    def unique_validator(self,postData):
        unique_errors = {}
        # check that the show title is unique
        unique_title = TVShow.objects.filter(title=postData['title'])
        if len(unique_title) > 0:
            unique_errors['title_name'] = "That show already exists"
        return unique_errors    



# Create your models here.
class TVShow(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TVShowManager()
            