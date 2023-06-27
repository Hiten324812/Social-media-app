from django.shortcuts import render
from .models import post
from .forms import postcreate
from django.contrib.auth.decorators import login_required


@login_required
def post_create(request):
    if request.method == 'POST':

        form = postcreate(data=request.POST,files=request.FILES)

        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()

    else:
        form = postcreate(data=request.GET)
    
    return render(request,'create.html',{'form' : form})

