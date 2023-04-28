from django.shortcuts import render

# Create your views here.

def main(request, page, action=""):
    print("testtt")
    return render(request, "role.html")