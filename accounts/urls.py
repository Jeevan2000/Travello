from django.urls import path

from . import views

urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('pune',views.pune,name='pune'),
    path('surat',views.surat,name='surat'),
    path('mumbai',views.mumbai,name='mumbai'),
    path('bengalaru',views.bengalaru,name='bengalaru')
    ]