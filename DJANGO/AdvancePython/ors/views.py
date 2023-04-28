from django.shortcuts import render, redirect
from django.http import HttpResponse
from ors.forms import MarksheetForm
from ors.models import Marksheet
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.views.decorators.cache import cache_control

# Create your views here.
def index(request):
    #return HttpResponse("Welcome to ORS")
    return render(request, "ors/index.html")


def home(request):
    return render(request, "ors/Welcome.html")


def add_marksheet(request):
    form=MarksheetForm()
    if request.method=="POST":
        form=MarksheetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Marksheet Added Successfully")
            return redirect("GET_ALL")
            #return HttpResponse("Marksheet Added")
    return render(request, "ors/Registration.html", context={"Mform":form})


def getAllData(request):
    objects=Marksheet.objects.all()
    return render(request, "ors/GetAllData.html", context={"Data":objects})


def edit(request, id):
    obj=Marksheet.objects.get(id=id)
    form=MarksheetForm(instance=obj)
    if request.method=="POST":
        form=MarksheetForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Marksheet Updated Successfully")
            return redirect("GET_ALL")
    return render(request, "ors/Edit.html", {"Form":form, "ID":id})


def delete_Marksheet(request, id):
    obj=Marksheet.objects.get(id=id)
    if request.method=="POST":
        obj.delete()
        messages.success(request, "Marksheet Deleted Successfully")
        return redirect("GET_ALL")
    return render(request, "ors/Delete.html", {"obj":obj})

def usersignUp(request):
    if request.method=="POST":
        # Get the UserData From 
        uname= request.POST["uname"]
        Fname= request.POST["Fname"]
        Lname= request.POST["Lname"]
        email= request.POST["email"]
        pwd= request.POST["pwd"]
        # Create User Object
        obj=User.objects.create_superuser(uname, email, pwd)
        obj.fname=Fname
        obj.lname=Lname
        obj.save()
        messages.success(request, "User Created Successfully")
        return render(request, "ors/Login.html")
    return render(request, "ors/UserRegistration.html")

def usersignIn(request):
    
    if request.method=="POST":
        # Get the UserData From 
        uname= request.POST["uname"]
        pwd= request.POST["pwd"]
        user=authenticate(username=uname, password=pwd)
        if user is not None:
            print("tewstttt")
            login(request,user)
            messages.success(request, "You are Logged in Successfully")
            return redirect("INDEX")
        else:
            print("yyyy")
            messages.warning(request, "Invalid User")
            return redirect("HOME")
    return render(request, "ors/Login.html")

def userSignOut(request):
    logout(request)
    messages.success(request, "You are SingOut in Successfully")
    return redirect("HOME")


def getSession(request):
    return HttpResponse(f"Session Id={request.session.session_key}")

# if You wand to write some data on browser side than use cookies 

def setCookies(request):
    res=HttpResponse("Cookies Enabled")
    res.set_cookie("Name","Rays",max_age=60)
    return res

# Next time you can fatch the cookies data using request object
@cache_control()
def getCookies(request):
    value=request.COOKIES.get("Name")
    return HttpResponse(f"Name={value}")

