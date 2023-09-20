from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home,name="home_page"),
    path("about/",views.about,name='about_page'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('admin/login/', auth_views.LoginView.as_view(), name='admin_login'),
    path('staff/',views.staff_view,name='user_dashbord'),
    path("principal/",views.princi, name="principal_dashbord"),
    path("superintendent/",views.superintendent_view , name="superintendent_dashbord")

]