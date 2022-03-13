from django.shortcuts import redirect, render
from .models import Emp, Post
from django.contrib import messages
# Create your views here.
#original pages
def home(request):
    return render(request,'home.html')

def show(request):
    posts=Post.objects.all()
    return render(request,'show.html',{'posts':posts})

def add(request):
    if request.method=='POST':
            title=request.POST['title']
            detail=request.POST['detail']
            Post.objects.create(title=title, detail=detail)
            messages.success(request,'Data has en added')
    return render(request,'add.html')

def update(request, id):
    if request.method=='POST':
            title=request.POST['title']
            detail=request.POST['detail']
            Post.objects.filter(id=id).update(title=title, detail=detail)
            messages.success(request,'Data has en added')
    post=Post.objects.get(id=id)
    return render(request,'update.html',{'post':post})

def delete(request, id):
    Post.objects.filter(id=id).delete()
    return redirect('/show')

#employee pages

def empshow(request):
    empposts=Emp.objects.all()
    return render(request,'empshow.html',{'empposts':empposts})

def empadd(request):
    if request.method=='POST':
            empid=request.POST['empid']
            detail=request.POST['detail']
            joindate=request.POST['joindate']
            Emp.objects.create(empid=empid, detail=detail, joindate=joindate)
            messages.success(request,'Employee Data has en added')
    return render(request,'empadd.html')

def empupdate(request, id):
    if request.method=='POST':
            empid=request.POST['empid']
            detail=request.POST['detail']
            joindate=request.POST['joindate']
            Emp.objects.filter(id=id).update(empid=empid, detail=detail, joindate=joindate)
            messages.success(request,'Employee Data has en added')
    emp=Emp.objects.get(id=id)
    return render(request,'empupdate.html',{'emp':emp})

def empdelete(request, id):
    Emp.objects.filter(id=id).delete()
    return redirect('/empshow')
