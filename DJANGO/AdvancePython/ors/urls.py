"""AdvancePython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from ors import views

urlpatterns = [
    #default Mapping
    path("", views.index, name="INDEX"),
    path("home/", views.home, name="HOME"),
    path("add/", views.add_marksheet, name="ADD"),
    path("getAll/",views.getAllData, name="GET_ALL"),
    path("edit/<int:id>",views.edit, name="EDITMarksheet"),
    path("delete/<int:id>",views.delete_Marksheet, name="EDIT_M"),
    path("signUp/", views.usersignUp, name="SIGN_UP"),
    path("signIn/", views.usersignIn, name="SIGN_IN"),
    path("signOut/", views.userSignOut, name="SIGN_OUT"),
    path("getSession/", views.getSession, name="Get_Session"),
    path("setCookies/", views.setCookies, name="Set_Cookies"),
    path("getCookies/", views.getCookies, name="Get_Cookies"),        
]

