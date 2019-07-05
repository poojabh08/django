from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
# Create your views here.
from home.forms import Studentsearchform,StudentEditModelForm,StudentCreateForm
from home.models import Student
from . forms import UserRegisterForm
def home_view(request):
    # form=Studentsearchform()
    # msg="hello form from django"
    # context={'form':form,'msg':msg}
    # return render(request,'home.html',context)
    # del request.session['id']
    # if request.session['id']=='1':
        if request.method=='POST':
            search=Studentsearchform(request.POST)
            #  print(search)
            if search.is_valid():
                value=search.cleaned_data.get('q')
                result=Student.objects.filter(student_name__contains=value)
                return render(request,'home1.html',{'result':result,'form':Studentsearchform()})
        else:
            form=Studentsearchform()
            result=Student.objects.all()
            return render(request,'home1.html',{'form':form,'result':result})
def home_view1(request):
    return render(request,'testpge.html')
def deletestudent(request,id):
    result=Student.objects.get(id=id)
    result.delete()
    messages.success(request,'Deleted Successfully!!')
    return redirect('/home/')   


def editstudent(request,id):
    request.session['id']=id
    student=Student.objects.get(id=id)
    if request.method=='POST':
        modelform=StudentEditModelForm(request.POST,instance=student)
        if modelform.is_valid():
            modelform.save()
            messages.success(request,'Edited Successfully')
            return redirect('/home/')
    else:
        modelform=StudentEditModelForm(instance=student)
        return render(request,'edit.html',{'form':modelform,'value':'edit'})

def createstudent(request):
    form=StudentCreateForm(request.POST)
    if form.is_valid():
        student=Student.objects.create(student_name=form.cleaned_data.get('student_name'),department=form.cleaned_data.get('department'))
        student.save()
        messages.success(request,'Created Successfully')
        return redirect('/home/')
    else:
        form=StudentCreateForm()
        return render(request,'create.html',{'form':form,'value':'create'})
# def about(request):
#     return render(request,'about.html')
# def contact(request):
#     return render(request,'contact.html')
def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_activate:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse('Your Account was inactive')
        else:
            print('Someone tried to login amd failed')
            print('they used username:{} password:{}'.format(username,password))
            return HttpResponse("Invalid login details given")
    else:
         return render(request,'auth/login.html',{})
def userlogout(request):
    logout(request)
    return redirect('/login/')
def userregister(request):
    registered=False
    if request.method=='POST':
        use_form=UserRegisterForm(request.POST)
        if use_form.is_valid():
            user=use_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
        else:
            print(use_form.errors)
    else:
        use_form=UserRegisterForm()
    return render(request,'auth/register.html',{'form':use_form,'registered':registered,'value':'Register'})
