from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
import uuid
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.utils.http import url_has_allowed_host_and_scheme
from .models import *
from base.emails import send_account_activation_email

# Create your views here.
def login_page(request):
    next_url=request.GET.get("next") 
    if request.method == "POST":
        username=request.POST.get("username")               
        password=request.POST.get("password")
        user_obj=User.objects.filter(username=username)
        
        if not user_obj.exists():
            messages.warning(request,"Account not found")
            return HttpResponseRedirect(request.path_info)
        
        if not user_obj[0].profile.is_email_verified:
            messages.error(request,"Email not verified")
            return HttpResponseRedirect(request.path_info)
        
        user_obj=authenticate(username=username,password=password)
        if user_obj:
            login(request,user_obj)
            messages.success(request,"Login Successful")        
            if url_has_allowed_host_and_scheme(url=next_url,allowed_hosts=request.get_host()):
                return redirect(next_url)
            else:
                return redirect(reverse("index"))

        messages.error(request,"Invalid credentials")
        return HttpResponseRedirect(request.path_info)
        
    return render(request,"accounts/login.html")    
        
def register_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        user_obj=User.objects.filter(username=username,email=email)
        
        if user_obj.exists():
            messages.info(request,"Username or Email already in use")
            return HttpResponseRedirect(request.path_info)
        
        user_obj=User.objects.create(
            username=username, first_name=first_name, last_name=last_name,email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        
        
        profile=Profile(user=user_obj)
        profile.email_token=str(uuid.uuid4())
        profile.save()

        send_account_activation_email(email, profile.email_token)
        print("Mail Sent")
        messages.success(request, "An email has been sent to your mail")
        return HttpResponseRedirect(request.path_info)
    return render(request, "accounts/register.html")

def activate_email_account(request, email_token):
    
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_email_verified = True
        user.save()
        messages.success(request, 'Account verification successful.')
        print("Account verification done")
        return redirect('login')
    
    except Exception as e:
        return HttpResponseRedirect('Invalid email token')
def password_reset(request):
    pass