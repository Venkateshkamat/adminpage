from django.db import models

# Create your models here.

class studenttable(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    img = models.ImageField(upload_to='Studentpics')
    age = models.IntegerField()

    def __str__(self):
        return self.firstname +" "+ self.lastname

    
    