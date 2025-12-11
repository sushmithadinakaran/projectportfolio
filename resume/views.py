from django.shortcuts import render,redirect
from .models import details

# Create your views here.
def home(request):
    return render(request ,"home.html")
def about(request):
    return render(request,"about.html")
def project(request):
    projects=[{'title':'Work Portfolio',
               'description':'My Portfolio showcases the project i"ve built using Python,Django,JavaScript,and modern web technologies.Each projects reflects my skills in backend development,frontend design,and problem-solving.I enjoy creating clean,functional, and user-friendly applications that solve real-world problems.',
               'used_techs':'HTML,Css,Bootstrap,Python,Django,Django ORM,SQLite,Git & Github,Vscode',
               'gitpath':'https://github.com/sushmithadinakaran/projectportfolio'},
        {'title':"Student Management Based On CRUD",
               'description':'The Student Management System is a simple CRUD-based web application designed to manage student records efficiently.It allows users (admin/teachers) to create read,update and delete student information through a clean and user friendly interface.This project demonstrates core backend development concepts using Djangoo and implements proper structuring',
               'used_techs':'Django Framework,Html,Css,Bootstrap(awesomeicons,modal),django ORM for database interactions,MVT architecture',
               'gitpath':'https://github.com/sushmithadinakaran/projectstudent'},
        {
         'title':"Patient Appointment Schedular",
         'description':'This project helps hospital staff handle patient apponitments with features like adding new apponitments and removing them instantly using JavaScript DOM.',        
         'used_techs':'Html,Css,js DOM',
         'gitpath':"https://github.com/sushmithadinakaran/projecthospitaldom"

        },
        {
            'title':"Student Data Entry",
            'description':'Developed a student information entry system,allows users to input student details and dynamically displays them in a structured table without refreshing the page.',
            'used_techs':'Html,Css,js DOM',
            'gitpath':"https://github.com/sushmithadinakaran/projecttutiondom"
        }
     ]
    return render(request,"project.html",{"projects":projects})
def contact(request):
    if request.method=="POST":
        uname=request.POST.get("name")  
        uemail=request.POST.get("email")
        umessage=request.POST.get("message")
        uphone_no=request.POST.get("phone_no")
        data=details.objects.create(name=uname,email=uemail,message=umessage,phone_no=uphone_no)
        return redirect("success")
        
    return render(request,"contact.html")
def success(request):
    return render(request,"success.html")
def certification(request):
    return render(request,"certification.html")
def resume(request):
    return render(request,"resume.html")

def base(request):
    return render(request,"base.html")
