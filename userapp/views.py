from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'userapp/home.html')
def base(request):
    return render(request,'userapp/base.html')
def about(request):
    return render(request,'userapp/about.html')
def jobs(request):
    return render(request,'userapp/jobs.html')
def posts(request):
    return render(request,'userapp/posts.html')
def contacts(request):
    return render(request,'userapp/contacts.html')



