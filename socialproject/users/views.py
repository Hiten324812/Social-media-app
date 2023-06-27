from django.shortcuts import redirect, render
from .forms import loginform,userregistrationform
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import profile
from .forms import usereditform,profileditform
from django.http import request
from hashlib import new
from post.models import post

# Create your views here.

def user_login(request):
    if request.method == "POST":
       
       form = loginform(request.POST)

       if form.is_valid():
          data = form.cleaned_data
          user = authenticate(
             request,username=data['username'], password = data['password'])
       
       if user is not None:
            login(request,user)
            return redirect('index')
       else:
            return redirect('login')
           
    
    else:

        form = loginform()
        return render(request,'login.html',{'form' : form})

@login_required  
def index(request):
        
        current = request.user
        
        all_post = post.objects.filter(user = current)
        return render (request,'home.html',{'all_post' : all_post})

def register(request):

    if request.method == 'POST':
        user_form = userregistrationform(request.POST)
        
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile.objects.create(user=new_user)
            return render(request,'register_done.html')
    else:
        user_form = userregistrationform()

    return render(request,'register.html',{'user_form' : user_form})
    
@login_required
def edit(request):
      if request.method == 'POST':
          
          user_form = usereditform(instance=request.user,data=request.POST)
          profile_form = profileditform(instance=request.user.profile,data=request.POST,files=request.FILES)

          if user_form.is_valid() and profile_form.is_valid():
              user_form.save()
              profile_form.save()
        
      else:
          
            user_form = usereditform(instance=request.user)
            profile_form = profileditform(instance=request.user.profile)
      
      return render(request,'edit.html', {'user_form' : user_form , 'profile_form' : profile_form})

