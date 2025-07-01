from django.urls import path
from . import views 

urlpatterns = [
    path('Signup/', views.Signup, name='signup'),      
    path('Signin/', views.Signin, name='signin'),
    path('Logout/', views.Logout, name='logout'),
]
