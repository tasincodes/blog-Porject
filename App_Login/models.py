from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile_pics')









class Employee(models.Model):
    name=models.CharField(max_length=230,default="true")
    dept=models.CharField(max_length=10)
    ph=models.CharField(max_length=10,default="+880")

    def __str__(self) -> str:
        return self.name

        # def __str__(self):
        #     return self.name

