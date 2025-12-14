from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name="welcome"),
    path('klist/', views.blogHome, name="k_home"),
    # path('login/', views.login, name="login")
    path('login/', auth_views.LoginView.as_view(template_name = "k_blog/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.signup, name="signup"),
    path('post-create/',views.create_post, name='post-create')
]