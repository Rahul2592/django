from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Welcome to Text Editing App")
    return render(request, "textEditing/index.html")

def textEdit(request):
    #data=request.GET.get("text")
    data=request.POST.get("text")
    action=request.POST.get("optype")
    output=""
    if(action.__eq__("Lower")):
        output=data.lower()
    elif(action.__eq__("Upper")):
        output=data.upper()
    else:
        output=data.title()

    #return HttpResponse(f"{output}")
    return render(request,"textEditing/output.html", context={"OUT":output,"Action":action})

def fullName(request):
        if request.method=="POST":
            fname=request.POST["fname"]
            lname=request.POST["lname"]
            fullName=fname+" "+lname
            return HttpResponse(f"Welcome :{fullName}")
        return render(request, "textEditing/Fname.html")


        

