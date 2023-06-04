import re
from sre_constants import SUCCESS
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    return render(request,'index.html')

def EmployeeSignup(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empCode']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=fn, last_name=ln,username=em,password=pwd)
            EmployeeDetail.objects.create(user = user,empcode=ec)
            EmployeeEducation.objects.create(user = user)
            EmployeeExperience.objects.create(user = user)
            EmployeeLeaves.objects.create(user = user)
            Loan.objects.create(user = user)
            Esalarye.objects.create(user = user)
            error = "no"
        except:
            error = "yes"         
    return render(request,'EmployeeSignup.html',locals())

def EmployeeLogin(request):
    error = ""
    if request.method == "POST":
        u = request.POST['emailid']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        if user:
            login(request,user)
            error = "no"
        else:
            error = "yes"
    return render(request,'EmployeeLogin.html',locals())

def EmployeeHome(request):
    if not request.user.is_authenticated:
        return redirect('EmployeeLogin')
    return render(request,'EmployeeHome.html')


def MyProfile(request):
    if not request.user.is_authenticated:
        return redirect('EmployeeLogin')
    error = ""
    user = request.user
    employee = EmployeeDetail.objects.get(user = user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empCode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']
        
        employee.user.first_name= fn
        employee.user.last_name= ln
        employee.empCode= ec
        employee.empdept= dept
        employee.designation= designation
        employee.contact= contact
        employee.gender= gender
        
        if jdate:
            employee.joiningdate = jdate
            
        try:
            employee.save()
            employee.user.save()
            error = "no"
        except:
            error = "yes"         
    return render(request,'MyProfile.html',locals())


def MyExperience(request):
    if not request.user.is_authenticated:
        return redirect('EmployeeLogin')
    user = request.user 
    experience = EmployeeExperience.objects.get(user = user)
    return render(request,'MyExperience.html',locals())


def MyEducation(request):
    if not request.user.is_authenticated:
        return redirect('EmployeeLogin')
    user = request.user 
    education = EmployeeEducation.objects.get(user = user)
    return render(request,'MyEducation.html',locals())


def EditeMyEducation(request):
    if not request.user.is_authenticated:
        return redirect('EmployeeLogin')
    error = ""
    user = request.user
    education = EmployeeEducation.objects.get(user = user)
    if request.method == "POST":
        coursepg = request.POST['coursepg']
        schoolclgpg = request.POST['schoolclgpg']
        yearofpassingpg = request.POST['yearofpassingpg']
        percentagepg = request.POST['percentagepg']
        
        coursepggra = request.POST['coursepggra']
        schoolclggra = request.POST['schoolclggra']
        yearofpassingra = request.POST['yearofpassingra']
        percentagegra = request.POST['percentagegra']
        
        coursessc = request.POST['coursessc']
        schoolclgssc = request.POST['schoolclgssc']
        yearofpassingssc = request.POST['yearofpassingssc']
        percentagessc = request.POST['percentagessc']
        
        coursehsc = request.POST['coursehsc']
        schoolclghsc = request.POST['schoolclghsc']
        yearofpassinghsc = request.POST['yearofpassinghsc']
        percentagehsc = request.POST['percentagehsc']
        
        education.coursepg = coursepg
        education.schoolclgpg= schoolclgpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg = percentagepg
        education.coursepggra = coursepggra
        education.schoolclggra= schoolclggra
        education.yearofpassingra = yearofpassingra
        education.percentagegra = percentagegra
        education.coursessc = coursessc
        education.schoolclgssc= schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagessc = percentagessc
        education.coursehsc = coursehsc
        education.schoolclghsc= schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagehsc = percentagehsc
        
              
        try:
            education.save()
            error = "no"
        except:
            error = "yes"         
    return render(request,'EditeMyEducation.html',locals())



def EditeMyExperience(request):
    if not request.user.is_authenticated:
        return redirect('EmployeeLogin')
    error = ""
    user = request.user
    experience = EmployeeExperience.objects.get(user = user)
    if request.method == "POST":
        company1name = request.POST['company1name']
        company1design = request.POST['company1design']
        company1salary = request.POST['company1salary']
        company1duration = request.POST['company1duration']
        company1durationto = request.POST['company1durationto']
        
        company2name = request.POST['company2name']
        company2design = request.POST['company2design']
        company2salary = request.POST['company2salary']
        company2duration = request.POST['company2duration']
        company2durationto = request.POST['company2durationto']
        
        company3name = request.POST['company3name']
        company3design = request.POST['company3design']
        company3salary = request.POST['company3salary']
        company3duration = request.POST['company3duration']
        company3durationto = request.POST['company3durationto']
        
        experience.company1name = company1name
        experience.company1design= company1design
        experience.company1salary = company1salary
        experience.company1duration = company1duration
        experience.company1durationto = company1durationto
        experience.company2name = company2name
        experience.company2design= company2design
        experience.company2salary = company2salary
        experience.company2duration = company2duration
        experience.company2durationto = company2durationto
        experience.company3name = company3name
        experience.company3design= company3design
        experience.company3salary = company3salary
        experience.company3duration = company3duration
        experience.company3durationto = company3durationto
        
              
        try:
            experience.save()
            error = "no"
        except:
            error = "yes"         
    return render(request,'EditeMyExperience.html',locals())


def EmployeeJobForm(request):
    return render(request,'EmployeeJobForm.html')



def EmployeeJobDetails(request):
    return render(request,'EmployeeJobDetails.html')

def EmployeeJobProfile(request):
    return render(request,'EmployeeJobProfile.html')

def Designations(request):
    return render(request,'Designations.html')

def Designations(request):
    if not request.user.is_authenticated:
        return redirect('EmployeeLogin')
    user = request.user
    employee = EmployeeDetail.objects.get(user = user)
    return render(request,'Designations.html',locals())

def Overtime(request):
    return render(request,'Overtime.html')

def Holidays(request):
    return render(request,'Holidays.html')

def loanpdf(request):
    return render(request,'loanpdf.html')

def MyLeaves(request):
    if not request.user.is_authenticated:
        return redirect('EmployeeLogin')
    user = request.user
    leaves = EmployeeLeaves.objects.get(user = user)
    return render(request,'MyLeaves.html',locals())


def EditMyLeaves(request):
    if not request.user.is_authenticated:
        return redirect('EmployeeLogin')
    error = ""
    user = request.user
    leaves = EmployeeLeaves.objects.get(user = user)
    if request.method == "POST":
        leaveType = request.POST['leaveType']
        fro = request.POST['fro']
        to = request.POST['to']
        description = request.POST['description']
        
        
        leaves.leaveType = leaveType
        leaves.fro = fro
        leaves.to = to
        leaves.description= description
                    
        try:
            leaves.save()
            error = "no"
        except:
            error = "yes"         
    return render(request,'EditMyLeaves.html',locals())


def ChangePassword(request):
    if not request.user.is_authenticated:
        return redirect('EmployeeLogin')
    error = ""
    user = request.user
    if request.method == "POST":      
        c = request.POST['currentpassword']  
        n = request.POST['newpassword']    
        try:
            if user.check_password(c):
                user.set_password(n)                
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"         
    return render(request,'ChangePassword.html',locals())


def Logout(request):
    logout(request)
    return render(request,'index.html')

                #------------------------------->ADMIN<-------------------------------#

def adminlogin(request):
    error = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        try:
            if user.is_superuser:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"    
    return render(request,'adminlogin.html',locals())


def adminhome(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    return render(request,'adminhome.html')


def admninchangepassword(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    error = ""
    user = request.user
    if request.method == "POST":      
        c = request.POST['currentpassword']  
        n = request.POST['newpassword']    
        try:
            if user.check_password(c):
                user.set_password(n)                
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"         
    return render(request,'admninchangepassword.html',locals())

def adminallemployee(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    employee = EmployeeDetail.objects.all()           
    return render(request,'adminallemployee.html',locals())

def delete_employee(request,pid):
    if not request.user.is_authenticated:
        return redirect('hrlogin')
    user = User.objects.get(id=pid)
    user.delete()           
    return redirect('adminallemployee')

def delete_loan(request,pid):
    if not request.user.is_authenticated:
        return redirect('hrlogin')
    user = User.objects.get(id=pid)
    user.delete()           
    return redirect('adminallemployee')

def adminedite_profile(request,pid):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    error = ""
    
    employee = EmployeeDetail.objects.get(id = pid)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empCode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']
        
        employee.user.first_name= fn
        employee.user.last_name= ln
        employee.empCode= ec
        employee.empdept= dept
        employee.designation= designation
        employee.contact= contact
        employee.gender= gender
        
        if jdate:
            employee.joiningdate = jdate
            
        try:
            employee.save()
            employee.user.save()
            error = "no"
        except:
            error = "yes"         
    return render(request,'adminedite_profile.html',locals())


def adminleave(request,pid):
    if not request.user.is_authenticated:
        return redirect('EmployeeLogin')
    error = ""
    user = User.objects.get(id=pid)
    leaves = EmployeeLeaves.objects.get(user = user)
    if request.method == "POST":
        leaveType = request.POST['leaveType']
        fro = request.POST['fro']
        to = request.POST['to']
        description = request.POST['description']
        
        
        leaves.leaveType = leaveType
        leaves.fro = fro
        leaves.to = to
        leaves.description= description
                    
        try:
            leaves.save()
            error = "no"
        except:
            error = "yes"         
    return render(request,'adminleave.html',locals())


def Department(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    error = ""
    user = request.user
    depa = Edepartment.objects.get(user = user)
    if request.method == "POST":
        dname = request.POST['dname']
        dhead = request.POST['dhead']
       
        depa.dname = dname
        depa.dhead= dhead
        
              
        try:
            depa.save()
            error = "no"
        except:
            error = "yes"         
    return render(request,'Department.html',locals())


def alldepartment(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    user = request.user 
    depa = Edepartment.objects.get(user = user)
    return render(request,'alldepartment.html',locals())

def adesignation(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    employee = EmployeeDetail.objects.all()           
    return render(request,'adesignation.html',locals())



def loandoc(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin')
    employee = Loan.objects.all()           
    return render(request,'loandoc.html',locals())





def Myloan(request):
    if not request.user.is_authenticated:
        return redirect('EmployeeLogin')
    user = request.user 
    educba = Loan.objects.get(user = user)
    return render(request,'Myloan.html',locals())


def editemyloan(request):
    if not request.user.is_authenticated:
        return redirect('EmployeeLogin')
    error = ""
    user = request.user
    educba = Loan.objects.get(user = user)
    if request.method == "POST":
        loanType = request.POST['loanType']
        amount = request.POST['amount']
        fro = request.POST['fro']
        to = request.POST['to']
        emi = request.POST['emi']
        
        
        educba.loanType = loanType
        educba.amount = amount
        educba.fro= fro
        educba.to = to
        educba.emi = emi
        
              
        try:
            educba.save()
            error = "no"
        except:
            error = "yes"         
    return render(request,'editemyloan.html',locals())







                #------------------------------->HR<-------------------------------#

def hrlogin(request):
    error = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        try:           
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error="yes"        
    return render(request,'hrlogin.html',locals())


def hrhome(request):
    if not request.user.is_authenticated:
        return redirect('hrlogin')
    return render(request,'hrhome.html')


def lead(request):
    return render(request,'lead.html')


def hrchangepassword(request):
    if not request.user.is_authenticated:
        return redirect('hrlogin')
    error = ""
    user = request.user
    if request.method == "POST":      
        c = request.POST['currentpassword']  
        n = request.POST['newpassword']    
        try:
            if user.check_password(c):
                user.set_password(n)                
                user.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"         
    return render(request,'hrchangepassword.html',locals())

def hrallemployee(request):
    return render(request,'hrallemployee.html')

def hrallemployee(request):
    if not request.user.is_authenticated:
        return redirect('hrlogin')
    employee = EmployeeDetail.objects.all()           
    return render(request,'hrallemployee.html',locals())

def hrdelete_employee(request,pid):
    if not request.user.is_authenticated:
        return redirect('hrlogin')
    user = User.objects.get(id=pid)
    user.delete()           
    return redirect('hrallemployee')

def hredite_employee(request,pid):
    if not request.user.is_authenticated:
        return redirect('hrlogin')
    error = ""
    employee = EmployeeDetail.objects.get(id = pid)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empCode']
        dept = request.POST['department']
        designation = request.POST['designation']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']
        
        employee.user.first_name= fn
        employee.user.last_name= ln
        employee.empCode= ec
        employee.empdept= dept
        employee.designation= designation
        employee.contact= contact
        employee.gender= gender
        
        if jdate:
            employee.joiningdate = jdate
            
        try:
            employee.save()
            employee.user.save()
            error = "no"
        except:
            error = "yes"         
    return render(request,'hredite_employee.html',locals())

def hrleave(request,pid):
    if not request.user.is_authenticated:
        return redirect('hrlogin')
    error = ""
    user = User.objects.get(id=pid)
    leaves = EmployeeLeaves.objects.get(user = user)
    if request.method == "POST":
        leaveType = request.POST['leaveType']
        fro = request.POST['fro']
        to = request.POST['to']
        description = request.POST['description']
        
        
        leaves.leaveType = leaveType
        leaves.fro = fro
        leaves.to = to
        leaves.description= description
                    
        try:
            leaves.save()
            error = "no"
        except:
            error = "yes"         
    return render(request,'hrleave.html',locals())

def Hdesignation(request):
    return render(request,'Hdesignation.html')




#------------------->JOB<-----------------#
def editmyjob(request):
    if not request.user:
        return redirect('editmyjob')
    error = ""
    user = request.user
    Job = EmployeeJob.objects.get
    if request.method == "POST":
        Position = request.POST['Position']
        no = request.POST['no']
        age = request.POST['age']
        city = request.POST['city']
        esalary = request.POST['esalary']
        osalary = request.POST['osalary']
        date = request.POST['date']
        
        Job.Position = Position
        Job.no = no
        Job.age= age
        Job.city= city
        Job.esalary= esalary
        Job.osalary= osalary
        Job.date= date
                    
        try:
            Job.save()
            error = "no"
        except:
            error = "yes"         
    return render(request,'editmyjob.html',locals())





def aboutus(request):
    return render(request,'aboutus.html')




#-------------- salary--------------------#



def MySalary(request):
    if not request.user.is_authenticated:
        return redirect('EmployeeLogin')
    user = request.user
    leavess = Esalarye.objects.get(user = user)
    return render(request,'MySalary.html',locals())



def Salary(request):
    if not request.user.is_authenticated:
        return redirect('EmployeeLogin')
    error = ""
    user = request.user
    leavess = Esalarye.objects.get(user = user)
    if request.method == "POST":
        bs = request.POST['bs']
        hra = request.POST['hra']
        pf = request.POST['pf']
        ot = request.POST['ot']
        at = request.POST['at']
        am = request.POST['am']
        
        
        leavess.bs = bs
        leavess.hra = hra
        leavess.pf = pf
        leavess.ot= ot
        leavess.at= at
        leavess.ot= am
                    
        try:
            leavess.save()
            error = "no"
        except:
            error = "yes"         
    return render(request,'Salary.html',locals())
