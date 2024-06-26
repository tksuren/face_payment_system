from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),  
    path('homebase/', views.homebase, name='homebase'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('main/',views.main,name='main'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('quick_pay/', views.quick_pay, name='quick_pay'),
    path('register_face/', views.register_face, name='register_face'),
   
]
