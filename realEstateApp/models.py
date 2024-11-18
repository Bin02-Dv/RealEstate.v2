from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=40, blank=True)
    number = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField(max_length=100, blank=True)
    
    def __str__(self):
        return f"send by {self.name}"
