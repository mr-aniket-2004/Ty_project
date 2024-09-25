from django.contrib import admin
from home.models import Contact,course,sign_up_table
from student.models import student_couser
# Register your models here.
admin.site.register(Contact)
admin.site.register(course)
admin.site.register(sign_up_table)