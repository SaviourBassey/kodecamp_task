from re import A
from django.urls import path
from .views import signup, login

urlpatterns = [
    path("signup/", signup), #section A
    path("login/", login), #section B
    #path("forget-password/", forgetpassword) #C
]


