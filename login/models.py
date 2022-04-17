from django.db import models

class user(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=8)
    
    def __str__(self):
        return self.username