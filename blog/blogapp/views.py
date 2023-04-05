from django.shortcuts import render,redirect
from . forms import SignUpForm, blog_form as bform
from django.contrib import messages
from . models import blog
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login as  us_login, logout as us_logout,update_session_auth_hash
from django.core.paginator import Paginator
# Create your views here.
def base(request):
    return render(request, 'base.html')

def home(request):
    d = blog.objects.all()
    P = Paginator(d,1)
    page_number = request.GET.get('page')
    final_data = P.get_page(page_number)
    return render(request,'home.html',{'data':final_data})

def signup(request):
    if request.method =='POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'You Have Register Succesfully !!')
            return redirect('login')
    else:
        fm = SignUpForm()
        return render(request,'signup.html',{'fm':fm})



def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            my_user = authenticate(request ,username=username, password=password)
            if my_user is not None:
                us_login(request,my_user)
                messages.success(request, ('You Have Been Logged In!'))
                return redirect('home')
            else:
                messages.success(request, ('Error Logging In - Please Try Again...'))
                return redirect('login')
                
                
    else:
        fm = AuthenticationForm()
        return render(request, 'login.html', {'fm':fm})
    
def logout(request):
    us_logout(request)
    return redirect('base')


def addblog(request):
    if request.method == 'POST':
        fm = bform(request.POST,request.FILES)
        if fm.is_valid():
            title = fm.cleaned_data['title']
            content = fm.cleaned_data['content']
            photo = fm.cleaned_data['photo']
            blog(content = content, title = title,photo=photo).save()
            messages.success(request,'add succesfully')
            return redirect('home')  
    else:
        fm = bform()
        return render(request,'addblog.html',{'fm':fm})
    
def showblog(request):
    d = blog.objects.all()
    return render(request,'showblog.html',{'data':d})


def edit(request,did):
    pk = blog.objects.get(id=did)
    if request.method == 'POST':
        fm = bform(request.POST,instance=pk)
        if fm.is_valid():
            title = fm.cleaned_data['title']
            content = fm.cleaned_data['content']
            blog(id = did ,content = content, title = title).save()
            messages.success(request,'add succesfully')
            return redirect('home')   
    else:
        fm = bform(instance=pk)
        return render(request,'edit.html',{'fm':fm})
    

def delete(request,did):
    d = blog.objects.get(id = did)
    d.delete()
    return redirect('home')
