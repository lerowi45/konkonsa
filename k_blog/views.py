from django.shortcuts import render,  redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import KPost
from .forms import PostForm

# Create your views here.
def home(request):
    #return HttpResponse("Welcome fellow konkonsani!")
    return render(request=request, template_name="k_blog/index.html")

def blogHome(request):
    all_post_list = KPost.objects.all()
    return render(request, "k_blog/blog_list.html", {'all_posts': all_post_list})

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

def create_post(request):
    form = PostForm()
    return render(request,"k_blog/create_post.html", {'form':form})