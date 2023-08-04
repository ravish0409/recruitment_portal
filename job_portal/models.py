 
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    skills_required = models.CharField(max_length=200)   
    experience_level = models.CharField(max_length=50)   
  

    def __str__(self):
        return self.title

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    skills = models.CharField(max_length=200)   
    experience = models.CharField(max_length=50)   
   

    def __str__(self):
        return self.name
