from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EmployeeDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    empcode = models.CharField(max_length=50)
    empdept = models.CharField(max_length=50,null=True)
    designation = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=50,null=True)
    joiningdate = models.DateField(null=True)
    def __str__(self):
        return self.user.username
    
class EmployeeEducation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    coursepg = models.CharField(max_length=100,null=True)
    schoolclgpg = models.CharField(max_length=200,null=True)
    yearofpassingpg = models.CharField(max_length=20,null=True)
    percentagepg = models.CharField(max_length=30,null=True)
    coursepggra = models.CharField(max_length=100,null=True)
    schoolclggra = models.CharField(max_length=200,null=True)
    yearofpassingra = models.CharField(max_length=20,null=True)
    percentagegra = models.CharField(max_length=30,null=True)
    coursessc = models.CharField(max_length=100,null=True)
    schoolclgssc = models.CharField(max_length=200,null=True)
    yearofpassingssc = models.CharField(max_length=20,null=True)
    percentagessc = models.CharField(max_length=30,null=True)
    coursehsc = models.CharField(max_length=100,null=True)
    schoolclghsc = models.CharField(max_length=200,null=True)
    yearofpassinghsc = models.CharField(max_length=20,null=True)
    percentagehsc = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.user.username
    
class EmployeeExperience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company1name = models.CharField(max_length=100,null=True)
    company1design = models.CharField(max_length=100,null=True)
    company1salary = models.CharField(max_length=100,null=True)
    company1duration = models.CharField(max_length=100,null=True)
    company1durationto = models.CharField(max_length=100,null=True)
    company2name = models.CharField(max_length=100,null=True)
    company2design = models.CharField(max_length=100,null=True)
    company2salary = models.CharField(max_length=100,null=True)
    company2duration = models.CharField(max_length=100,null=True)
    company2durationto = models.CharField(max_length=100,null=True)
    company3name = models.CharField(max_length=100,null=True)
    company3design = models.CharField(max_length=100,null=True)
    company3salary = models.CharField(max_length=100,null=True)
    company3duration = models.CharField(max_length=100,null=True)
    company3durationto = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.user.username 
    
   
class EmployeeLeaves(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    leaveType = models.CharField(max_length=100,null=True)
    fro = models.DateField(null=True)
    to  = models.DateField(null=True)
    description = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.user.username  
      
    
class Loan(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    loanType = models.CharField(max_length=100,null=True)
    amount = models.CharField(max_length=100,null=True)
    fro = models.DateField(null=True)
    to  = models.DateField(null=True)
    emi = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.user.username 
        

class EmployeeJob(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Position = models.CharField(max_length=100,null=True)
    no = models.CharField(max_length=100,null=True)
    age = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    esalary = models.CharField(max_length=100,null=True)
    osalary = models.CharField(max_length=100,null=True)
    date = models.DateField(null=True)
    def __str__(self):
        return self.user.username    
    
    
class Edepartment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    dname = models.CharField(max_length=100,null=True)
    dhead = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.user.username     
 
  

class Esalarye(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bs = models.CharField(max_length=100,null=True)
    hra = models.CharField(max_length=100,null=True)
    pf = models.CharField(max_length=100,null=True)
    ot= models.CharField(max_length=100,null=True)
    at = models.CharField(max_length=100,null=True)
    am  = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.user.username    

    

    
    