from django.db import models
import datetime
from django.db import models
from django.contrib.auth.models import User
class user_details(models.Model):
    first_name=models.CharField(max_length=25,default="Please provide")
    last_name=models.CharField(max_length=25,default="Please provide")
    current_sem=models.IntegerField(default=1)
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    isallowed=models.BooleanField(default=False)
    homecity=models.CharField(max_length=30,default="Nadiad")
    Place_of_birth=models.CharField(max_length=30,default="Nadiad")
    dob=models.DateField(default=datetime.date.today)
    cgpa_till_6_sem=models.FloatField(default=3.0)
    image=models.ImageField(upload_to="login/images",default="")

    def __str__(self):
        return self.first_name+" "+self.last_name
    
