from django.contrib import admin
from django.urls import path
from teacher import views
# from home import views


urlpatterns = [
   path("teach",views.index1,name='teachdash'),
   
#    path("log",views.student_logout,name='log'),
]