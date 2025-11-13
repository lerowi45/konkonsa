from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("Welcome fellow konkonsani!")
    return render(request=request, template_name="k_blog/index.html")

def blogHome(request):
    return render(request=request, template_name="k_blog/blog_list.html")

