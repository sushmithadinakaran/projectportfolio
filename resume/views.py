from django.shortcuts import render,redirect
from .models import details

# Create your views here.
def home(request):
    return render(request ,"home.html")
def about(request):
    return render(request,"about.html")
def project(request):
    projects=[
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
