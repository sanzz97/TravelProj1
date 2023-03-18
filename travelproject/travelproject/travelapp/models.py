from django.db import models

# Create your models here. #Here we will create tables for database
# After you make any changes to model file, use command: python manage.py makemigrations
#to reflect the table in sqldb use command: python manage.py migrate
class Place(models.Model): #place - table name,
    name = models.CharField(max_length=250) #to store name
    img = models.ImageField(upload_to='pics') #we are saying where to upload the images ie: pics -- folder name
    desc = models.TextField() #for long msgs/content use textfield

    # Important -- After you make any changes to model file, use command: python manage.py makemigrations
    # to reflect the table in sqldb use command: python manage.py migrate


    def __str__(self):
        return self.name   # instead of objects, if we want only the names

class Team(models.Model):
    img1 = models.ImageField(upload_to='pics')
    name1 = models.CharField(max_length=250)
    desc1 = models.TextField()


