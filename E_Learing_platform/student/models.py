from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from home.models import course 


class student_couser(models.Model):
    core_subject = models.OneToOneField(course,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.core_subject.product_name