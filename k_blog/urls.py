from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="welcome"),
    path('klist/', views.blogHome, name="k_home"),
    path('login/', views.login, name="login")
]