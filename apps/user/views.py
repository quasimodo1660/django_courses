from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages

from .models import *

# Create your views here.
def login(request):
    return render(request,'user/index.html')

def register(request):  
    return render(request,'user/regit.html')


def loginP(request):
    if request.method == 'POST':
        errors=User.objects.login_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/login')
        else:
            request.session['user_id']=User.objects.get(email_address=request.POST['mail']).id
            return redirect('/wall')
       
    
    else:
        return redirect('/login')

def regiP(request):
    if request.method == 'POST':
        errors=User.objects.register_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                print tag
                messages.error(request, error, extra_tags=tag)
                if tag=='warning':
                    return redirect('/login')
            return redirect('/register')
        else:
            User.objects.create(first_name=request.POST['fName'],
                                last_name=request.POST['lName'],
                                password=bcrypt.hashpw(request.POST['psd1'].encode(), bcrypt.gensalt()),
                                email_address=request.POST['mail'],
                                phone=request.POST['pnum'],
                                DOB=request.POST['dob'])           
            request.session['user_id']=User.objects.last().id
            return redirect('/wall')
    else:
        return redirect('/register')

def show(request):
    user=User.objects.get(id=request.session['user_id'])
    print user.first_name
    return render(request,'user/user_info.html',{'user':user})

def logout(request):
    request.session.clear()
    return redirect('/login')