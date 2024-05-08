from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category (models.Model):
    category = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,blank=True)
    
    def __str__(self) -> str:
        return f"{self.category}"

class Expence(models.Model):
    expence_name  = models.CharField(max_length=100, null=True, blank=True)
    amount  = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    
    
    def __str__(self) -> str:
        return f"user:{self.user.username} name:{self.expence_name} category:{self.category}"