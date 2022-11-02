from multiprocessing import AuthenticationError
from django.shortcuts import render,redirect
from datetime import datetime, timedelta
from .forms import SignUpForm,LogInForm,ProfileForm,UserForm
from django.contrib.auth import login,logout
from django.contrib import messages
from .models import Profile,Mynetwork
from django.contrib.auth.models import User
from articles.models import Articles,WorkoutCalendar,Calendar
from django.utils.safestring import mark_safe
from datetime import date
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def myprofile(request,slug):
    user= User.objects.get(username=slug)
    profile= Profile.objects.get(user=user)
    workouts = Articles.objects.filter(author=profile)
    myprofile =Profile.objects.get(user=request.user)
    
    
    current_year = date.today().year
    current_month =date.today().month 
        
   
   
    cal = Calendar(profile.id,current_year,current_month)
    html_cal = cal.formatmonth(withyear=True)
    #context['calendar'] = mark_safe(html_cal)
    
    context={'pagetitle':'Profile','profile':profile,'myprofile':myprofile,'calendar':mark_safe(html_cal) }

    return render (request,"accounts/profile.html",context)

def signup_view(request):
    if request.method == 'POST':
        form =SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.save()
            login(request,user) 
            messages.success(request, ("Account created successfully"))
            return redirect('edit_profile')
        else:
            context={
                'form':form,
            }
            messages.error(request, ("Please enter Required details"))
            return render(request ,'accounts/signup.html',context)
    else:
            form=SignUpForm()
            context={
                'form':form,
            }
            return render(request ,'accounts/signup.html',context)

def login_view(request):
    if request.method == 'POST':
        form =LogInForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                messages.success(request, ("You were succesfully logged in"))
                return redirect(request.POST.get('next'))
            else:
                messages.success(request, ("You were succesfully logged in"))
                return redirect('allarticles')
            
    else:
        form=LogInForm()

    context={
                'form':form,

    }

    return render(request ,'accounts/login.html',context)

    return render (request,"accounts/profile.html")

def logout_view(request):
    logout(request)
    return redirect ('allarticles')
@login_required(login_url='login')
def edit_profile(request):
    myprofile= Profile.objects.get(user_id=request.user.id)
    print   ('1')
    if request.method == 'POST':
        print   ('2')
        editform = ProfileForm(request.POST,instance=myprofile)
       

        if editform.is_valid():
            editform.save()
            print   ('3')
            return redirect('edit_profile')
        
        else:
            print   ('4b')
            context={
                 'pagetitle':'Edit profile',
                'user_profile':user_profile,
                'editform':editform,

            }
            messages.success(request, ("Please enter Required details"))
            return render (request,"accounts/edit_profile.html",context) 
    else:
            print   ('2a1')
            editform=ProfileForm(instance=myprofile)
            user_profile=UserForm(instance=request.user)
            context={
                'pagetitle':'Edit profile',
                'editform':editform,
                'myprofile':myprofile,
                'user_profile':user_profile
            }
            print   ('3a')
            return render (request,"accounts/edit_profile.html",context) 

@login_required(login_url='login')
def userupdate(request):
        if request.method == 'POST':
            print('upodate')
            user_profile= UserForm(request.POST,instance=request.user)
            if user_profile.is_valid():
                user_profile.save()
                print   ('4c')
                return redirect('edit_profile')
            else:
                context={
                    'user_profile':user_profile,
                }
                messages.success(request, ("Please enter Required details"))
                return render (request,"accounts/edit_profile.html",context)

@login_required(login_url='login')
def follow(request,account):
        profile =Profile.objects.get(id=account)
        usernetwork=Mynetwork.objects.get(user=profile) 
        myprofile=Profile.objects.get(id=request.user.id)
        print(myprofile)
        mynetwork=Mynetwork.objects.get(user=myprofile)    
        
        if profile  not in mynetwork.follow.all():
            Mynetwork.add_follower(self=mynetwork,account=profile) 
            messages.success(request, ("Successfully followed user."))
            usernetwork.myfollowers.add(myprofile)
        return redirect ('profile',profile.user.username)
@login_required(login_url='login')       
def unfollow(request,slug):
        profile =Profile.objects.get(id=slug)
        userfollower=Mynetwork.objects.get(user=profile) 
        myprofile=Profile.objects.get(id=request.user.id)
        myfollowers=Mynetwork.objects.get(user=myprofile)
        #if profile in myfollowers.follow.all():
        unfollow=Mynetwork.remove_follower(self=myfollowers,account=profile)  
        messages.success(request, ("Successfully unfollowed User. "))
        userfollower.myfollowers.remove(myprofile)
        return redirect ('profile',profile.user.username)

        