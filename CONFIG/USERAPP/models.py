from django.db import models
from django.contrib.auth.models import User


class CustomerModel(models.Model):
    user      = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100,null=False,blank=False)
    lastName  = models.CharField(max_length=100,null=False,blank=False)
    email     = models.CharField(max_length=200,null=False,blank=False)

    def __str__(self):
        return self.firstName
