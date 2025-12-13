from django.shortcuts import render,  redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def home(request):
    #return HttpResponse("Welcome fellow konkonsani!")
    return render(request=request, template_name="k_blog/index.html")

def blogHome(request):
    return render(request=request, template_name="k_blog/blog_list.html")

# def login(request):
#     return render(request=request, template_name="k_blog/login.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome')
    else:
        form = UserCreationForm
    return render(request,"k_blog/signup.html", {'form':form})