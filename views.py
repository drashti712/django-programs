from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Student

def homepageview(request):
    return render(request,'home.html')

def aboutpageview(request):
    return render(request,'about.html')

def contactpageview(request):
    return render(request,'contact.html')

def myform(request):
    return render(request,'myform.html')

def reg(request):
    return render(request,'reg.html')

def process(request):
    print("Welcome")
    print(request.method)
    print(request.POST)
    a = int(request.POST['txt1'])
    b = int(request.POST['txt2'])
    c = a + b
    print(c)
    return render(request,'ans.html',{'mya':a,'myb':b,'mysum':c})

class studentlist(ListView):
    model = Student
    template_name = 'slist.html'