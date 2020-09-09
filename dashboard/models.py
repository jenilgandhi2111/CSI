from django.db import models
from django.contrib.auth.models import User
import datetime
class expert_in(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    exper_field=models.CharField(max_length=30)

    def __str__(self):
        return self.exper_field

class placement_companies(models.Model):
    logo=models.ImageField(upload_to="dashboard/placement_img",default="")
    Company_name=models.CharField(max_length=30)
    Description=models.CharField(max_length=100)
    Job_role=models.CharField(max_length=30)
    Job_role_description=models.CharField(max_length=30)
    Contract_based=models.BooleanField(null=True)
    Salary_offered=models.IntegerField(null=True)
    Salary_in=models.CharField(max_length=10,default="LPA",null=True)
    cgpa_required=models.FloatField(default=3.5,null=True)
    Role_no_available=models.IntegerField(null=True)
    available_till=models.DateField(default=datetime.date.today,null=True)
    
    def __str__(self):
        return self.Job_role+" "+self.Company_name
    




class Internship_companies(models.Model):
    logo=models.ImageField(upload_to="dashboard/internship_img",default="")
    Company_name=models.CharField(max_length=30)
    Description=models.CharField(max_length=100)
    Job_role=models.CharField(max_length=30)
    Job_role_description=models.CharField(max_length=30)
    Contract_based=models.BooleanField(null=True)
    Salary_offered=models.IntegerField(null=True)
    Salary_in=models.CharField(max_length=10,default="LPA",null=True)
    available_till=models.DateField(default=datetime.date.today,null=True)
    Role_no_available=models.IntegerField(default=0,null=True)
    cgpa_required=models.FloatField(default=3.5,null=True)
    
    def __str__(self):
        return self.Job_role+" "+self.Company_name

    
class gives(models.Model):
    company=models.CharField(max_length=30)

class new_class_placement(models.Model):
    company_name=models.CharField(max_length=50,null=True)
    offer_id=models.ForeignKey(placement_companies,on_delete=models.CASCADE,null=True)
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    stipend=models.IntegerField(default=2500)
    message=models.TextField(default="provide please")

    def __str__(self):
        return self.company_name
    def get_sal(self):
        return self.offer_id.Salary_offered
    

    