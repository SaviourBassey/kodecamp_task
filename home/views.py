from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home/index.html")


def about(request):
    return HttpResponse("<h1> About page</h1>")

def contact(request):
    return HttpResponse("<h1> contact page</h1>")
