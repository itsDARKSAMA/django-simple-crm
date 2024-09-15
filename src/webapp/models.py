from django.db import models
from datetime import date

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=50)
    crated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Record(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField(auto_now=False)
    category = models.ForeignKey(Category , on_delete=models.SET_NULL , null = True)
    weight = models.IntegerField()
    tall = models.IntegerField()
    mobile = models.CharField(max_length=13)
    address= models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    #--(a.almajayda) : Get record age by calculating birthdate  
    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
    

    def __str__(self):
        return f"{self .first_name} {self.last_name} - {self.get_age()} years old"
    
    #--(a.almajayda) : reordering records by creation date [created_date]
    class Meta:
        ordering = ["-created_at"]