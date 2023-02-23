from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm,CourseForm
from django.contrib.auth import authenticate, login, logout
from .models import Student,User,Course,Topic


# Create your views here.

def home(request):
    return render(request, 'home.html')


def log_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    if request.method == 'POST':
        form = LoginForm(request.POST, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pword = form.cleaned_data['password']
            user = authenticate(username=uname, password=pword)
            if user is not None:
                login(request, user)

            return redirect('course_list')
        return redirect('home')


def course_list(request):
    if request.method == 'GET':
        user = request.user
        data = Student.objects.get(user=user)
        courses=data.course.all()
        print(courses)
        # courses=[course.name for course in courses]
        # for course in cources:
        #     print(course.name)
        return render(request, 'course_list.html', {'courses': courses})
    
def create_course(request):
    if request.method=='GET':
        form=CourseForm()
        return render(request,'create_course.html',{'form':form})
    
    if request.method == 'POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')



    
def course_detail(request,pk):
    if request.method=='GET':
        course_data=Course.objects.get(id=pk)
        print(course_data)
        return render(request,'course_Detail.html',{'course_data':course_data})
    
def more_course(request):
    if request.method=='GET':
        data=Course.objects.all()
        print(data)
        return render(request,'more_course.html',{'data':data})

def add_course(request,pk):
    if request.method=='GET':
        add_data=Course.objects.get(id=pk)
        print(add_data)
        user=Student.objects.get(user=request.user)
        user.course.add(add_data)
        user.save()
        courses=user.course.all()
        return render(request,'course_list.html',{'courses':courses})
    
def delete_course(request,pk):
    if request.method=='GET':
        delete_data=Course.objects.get(id=pk)
        print(delete_data)
        user=Student.objects.get(user=request.user)
        user.course.remove(delete_data)
        user.save()
        courses=user.course.all()
        return render(request,'course_list.html',{'courses':courses})    
    
    
    

    


