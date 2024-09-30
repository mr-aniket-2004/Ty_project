from django.contrib import admin
from django.urls import path
from student import views
# from home import views


urlpatterns = [
   path("/student",views.index1,name='dashboard'),
   path("/feedback",views.feedback_info, name="feedback_info"),
   path("/course",views.student_cour, name="student_course"),
   path("/course/temp",views.temp , name='temp'),
   path("/course/temp/<slug>",views.temp , name='temp'),
   path("/course/temp/checkout/<slug:slug>",views.checkout,name="checkout"),
   path("/assignment",views.assignment,name="assignment"),
   path("/chat",views.chat,name="chat"),
   path("/help",views.help,name="help"),
   path("/profile",views.profile,name="profile"),
   path("/course/mycourse",views.mycourse,name="mycourse")
   
#    path("log",views.student_logout,name='log'),
]