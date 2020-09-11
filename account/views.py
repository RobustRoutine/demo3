from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import teacher_timetable
from django.conf import settings
from django.template.loader import render_to_string
import random as r
from django.urls import reverse
from .forms import teacher_timetableform



# Create your views here.
b=0
print(b)

def login(request):
    if request.method == "POST":

        email=request.POST['t1']
        password=request.POST['t2']


        if User.objects.filter(email=email).exists():


            return HttpResponseRedirect('tymtable')
        else:
            msg="user not exist"
            return render(request, 'account/msg.html', {"msg": msg})

    else:

        return render(request,'account/login.html')



def register(request):
    if request.method == "POST":
        username=request.POST['s1']
        email=request.POST['s2']
        password=request.POST['s3']
        #otp=request.POST['s4']
        n=5
        min=pow(10,n-1)
        max=pow(10,n)-1
        b=r.randint(min,max)
        b=str(b)
        print(b)
        user=authenticate(request,username=username,password=password)
        if User.objects.filter(email=email).exists():
            msg="Email-Id Exist"
            return render(request, 'account/msg.html', {"msg": msg})
        elif User.objects.filter(username=username).exists():
            msg="Username Exist"
            return render(request, 'account/msg.html', {"msg": msg})
        elif len(password) < 8:
            msg="Password is too short"
            return render(request, 'account/msg.html',{"msg":msg})
        else:

            #if not request.user.email.endswith('@jmit.ac.in'):
             #   print('4')
            #else:
             #   print('5')
            email_body="hi "+username+\
                       "\" To verify your email-id, use this security " \
                                     "code:"+b+\
                       "If you didn't requested for this code you can safely ignore this email ." \
                       "Someone else might have typed this email-id by mistake." \
                       "Thankyou "

            send_mail(
                'Account verification' ,
                email_body,
                'from@example.com',
                [email],
                fail_silently=False,
            )
            #if otp==b:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()


            return render(request, 'account/login.html')
            #redirect('/tymtable',{'user':user})

    else:
        return render(request, 'account/register.html')



def home(request):

    return render(request,'account/home.html')
def contact(request):
    return render(request,'account/contact.html')

def about(request):
    return render(request,'account/about.html')

def tutorial(request):

    return render(request,'account/tut_vedio.html')

def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def tymtable(request):
    teacher =teacher_timetable.objects.all()
    #teacher=teacher_timetable.objects.filter(user.username)
    return render(request, 'account/tymtable.html', {'teacher': teacher})

@login_required
def delete(request,id):
    teacher_timetable.objects.get(id=id)
    teacher_timetable.delete()
    return redirect(request,'account/tymtable.html')

@login_required()
def update(request,id):
    print('h1')
    teacher=teacher_timetable.objects.get(id=id)
    print('h2')
    form=teacher_timetableform(instance=teacher)
    print('h3')
    if request.method=='POST':
        form=teacher_timetableform(request.POST,instance=teacher)
        if form.is_valid:
            form.save()
        return redirect('/tymtable')
    context={'form':form}
    print('h4')
    return render(request,'account/edit.html',context)