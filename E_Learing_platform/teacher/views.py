from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.
def index1(request):
    return render(request,"teacherdesh.html")


def student_logout(request):
    logout(request)
    return render(request,"login.html")
    # return HttpResponse("back to home")
