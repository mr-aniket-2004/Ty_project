from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from home.models import sign_up_table ,course
from student.models import usercourse,helpquary
# Create your views here.

def index1(request):
    return render(request,"studentdashboard.html")


def student_logout(request):
    logout(request)
    return render(request,"login.html")
    # return HttpResponse("back to home")


def update_info(request):
    context ={}
    data = sign_up_table.objects.get(main__id=request.user.id)
    # print(data)
    context["data"]=data
    if request.method == "POST":
        print(request.POST)
        # print(request.file)
        profile_pic = request.POST.get('profile-photo')
        email= request.POST.get('Email')
        frist_name= request.POST.get('Frist_Name')
        last_name = request.POST.get('Last_Name')
        add = request.POST.get('Address')
        city = request.POST.get('City')
        state = request.POST.get('State')
        pincode = request.POST.get('Pincode')
        mo=request.POST.get('no')
        parent_no = request.POST.get('p_no')
        qualification = request.POST.get('Qualification')
        college = request.POST.get('College')

        urs = User.objects.get(id=request.user.id)
        urs.first_name=frist_name
        urs.last_name=last_name
        urs.email=email
        urs.save()

        data.mobile=mo
        data.add = add
        data.city_name =city
        data.state = state
        data.pincode =pincode
        data.p_mobile =parent_no
        data.qualification =qualification
        data.collge_name =college
        data.save()

        if "profile-photo" in request.FILES :
            img = request.FILES["profile-photo"]
            data.profile_pic =img
            data.save()

        context["status"]= "Changes save Successfully "
    return render(request, "update_form.html" ,context)
    # return HttpResponseRedirect('update_info')

def feedback_info(request):
    return render(request, "feedbackform.html")


def student_cour(request):
    all = course.objects.all()
    context ={
        'all':all
    }
    return render(request,"student_course.html",context)

def temp(request,slug):
    new_course = course.objects.filter(new_slug=slug)
    data ={
        "new" :new_course,
    }
    return render(request,"course_info.html",data)


def checkout(request,slug):
    sub = course.objects.get(new_slug=slug)
    # if sub.price == 0:
    #     sub = usercourse(
    #         user = request.user,
    #         sub = sub,
    #     )
    #     sub.save()
        # return redirect('dashboard')
    context ={
        "sub":sub,
    }
    if request.method  == "POST":
        c_name = request.POST.get('coursename')
        c_duration = request.POST.get('duration')
        c_price = request.POST.get('price')
        print(c_name,c_duration,c_price)
    return render(request,"checkout.html",context)

def assignment(request):
    return render(request,"assignment.html")


def chat(request):
    return render(request,"chat_with_teacher.html")

def help(request):
    if request.method == "POST":
        student_name = request.POST.get('name')
        student_email = request.POST.get('email')
        student_message = request.POST.get('message')
        print(student_name,student_email,student_message)
        myque= helpquary(student_name=student_name,student_email=student_email,student_message=student_message)
        myque.save()
    return render(request,"support.html")
    
def profile(request):
    return render(request,"profile.html")
