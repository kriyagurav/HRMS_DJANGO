from django import views
from django.contrib import admin
from django.urls import path,include
from app.views import *

urlpatterns = [
    #--------->Employee dasckbord<--------------
    path('',index,name='index'),
    path('EmployeeSignup/',EmployeeSignup,name='EmployeeSignup'),
    path('EmployeeLogin/',EmployeeLogin,name='EmployeeLogin'),
    path('EmployeeHome/',EmployeeHome,name='EmployeeHome'),
    path('EmployeeJobForm/',EmployeeJobForm,name='EmployeeJobForm'),
    path('EmployeeJobDetails/',EmployeeJobDetails,name='EmployeeJobDetails'),
    path('EmployeeJobProfile/',EmployeeJobProfile,name='EmployeeJobProfile'),
    path('MyProfile/',MyProfile,name='MyProfile'),
    path('MyExperience/',MyExperience,name='MyExperience'),
    path('EditeMyExperience/',EditeMyExperience,name='EditeMyExperience'),
    path('MyEducation/',MyEducation,name='MyEducation'),
    path('EditeMyEducation/',EditeMyEducation,name='EditeMyEducation'),
    path('Department/',Department,name='Department'),
    path('Designations/',Designations,name='Designations'),
    path('Overtime/',Overtime,name='Overtime'),
    path('Holidays/',Holidays,name='Holidays'),
    path('MyLeaves/',MyLeaves,name='MyLeaves'),
    path('EditMyLeaves/',EditMyLeaves,name='EditMyLeaves'),
    path('ChangePassword/',ChangePassword,name='ChangePassword'),
    path('MySalary/',MySalary,name='MySalary'),
    path('Salary/',Salary,name='Salary'),
    path('editemyloan/',editemyloan,name='editemyloan'),
    path('Myloan/',Myloan,name='Myloan'),
    path('loandoc/',loandoc,name='loandoc'),
    path('loanpdf/',loanpdf,name='loanpdf'),
    path('Logout/',Logout,name='Logout'),
    
    
    #------------>ADMIN<-----------#
    
    path('adminlogin/',adminlogin,name='adminlogin'),
    path('adminhome/',adminhome,name='adminhome'),
    path('admninchangepassword/',admninchangepassword,name='admninchangepassword'),
    path('adminallemployee/',adminallemployee,name='adminallemployee'),
    path('adesignation/',adesignation,name='adesignation'),
    path('alldepartment/',alldepartment,name='alldepartment'),
    path('delete_employee/<int:pid>',delete_employee,name='delete_employee'),
    path('adminedite_profile/<int:pid>',adminedite_profile,name='adminedite_profile'),
    path('adminleave/<int:pid>',adminleave,name='adminleave'),

    #------------>HR<-----------#
    
    path('hrlogin/',hrlogin,name='hrlogin'),
    path('hrhome/',hrhome,name='hrhome'),
    path('hrallemployee/',hrallemployee,name='hrallemployee'),
    path('lead/',lead,name='lead'),
    path('Hdesignation/',Hdesignation,name='Hdesignation'),
    path('hrchangepassword/',hrchangepassword,name='hrchangepassword'),
    path('hrdelete_employee/<int:pid>',hrdelete_employee,name='hrdelete_employee'),
    path('hredite_employee/<int:pid>',hredite_employee,name='hredite_employee'),
    path('hrleave/<int:pid>',hrleave,name='hrleave'),
    
    #------------>JOB<-----------#
    
    path('editmyjob/',editmyjob,name='editmyjob'),
    path('aboutus/',aboutus,name='aboutus'),

    
]
