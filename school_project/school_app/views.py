from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Teacher,Student
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages


# Create your views here.
def login1(request):
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['psw']
        user=authenticate(request,username=u,password=p)
        print(user)
        if user is not None and user.is_superuser==1:
            login(request,user)
            u=user.username
            return render(request,'admin_home.html',{'name':u})
        elif Student.objects.filter(Username=u,Password=p).exists():
            x=Student.objects.filter(Username=u,Password=p)
            for i in x:
                if i.value==1:
                    request.session['stud_id']=i.id
                    s=request.session['stud_id']
                    student=Student.objects.get(id=s)
                    return render(request,'stud_home.html',{'student':student})
                else:
                    messages.info(request,f'Admin not accepted you!')
                    return redirect(login1)
        elif Teacher.objects.filter(Username=u,Password=p).exists():
            y=Teacher.objects.filter(Username=u,Password=p)
            for i in y:
                request.session['teacher_id']=i.id
                t=request.session['teacher_id']
                teacher=Teacher.objects.get(id=t)
                return render(request,'teacher_home.html',{'teacher':teacher})
        else:
            messages.info(request,f'invalid username and password')
            return redirect(login1)

    else:
           return render(request,'login.html')
    
def logout(request):
    return redirect(login1)
def adminhome(request):
    return render(request,'admin_home.html')
def teacherhome(request):
    return render(request,'teacher_home.html')
def studenthome(request):
    return render(request,'stud_home.html')
def Home(request):
    return render(request,'Homepage.html')
        
def regteacher(request):
    if request.method=='POST':
        name=request.POST['nm']
        email=request.POST['em']
        mobile=request.POST['mob']
        uname=request.POST['uname']
        password=request.POST['psw']
        subject=request.POST['sub']
        Teacher.objects.create(Name=name,Email=email,Phone_no=mobile,user_type="Teacher",value=1,Username=uname,Password=password,Subject=subject)
        messages.info(request,f'registered')
        return redirect(regteacher)
    else:
         return render(request,'teacher_register.html')
def studregister(request):
    if request.method=='POST':
        name=request.POST['nm']
        email=request.POST['em']
        uname=request.POST['uname']
        password=request.POST['psw']
        class1=request.POST['cls']
        gender=request.POST['gend']
        phon_no=request.POST['ph']
        address=request.POST['ad']
        Student.objects.create(Name=name,Email=email,Gender=gender,Address=address,Phone_no=phon_no,user_type="student",value=0,Username=uname,Password=password,cls=class1)
        messages.info(request,f'registered')
        return redirect(studregister)
        # return HttpResponse("okk")
        
    else:
        return render(request,'stud_register.html')
    
def approve(request,sid):
    a=Student.objects.filter(id=sid).update(value=1)
    return redirect(studentview)
 

def studentview(request):
    a=Student.objects.filter(value=0)
    return render(request,'approve_students.html',{'a1':a})

def viewteacher(request):
    a=Teacher.objects.all()
    return render(request,'view_teacher.html',{'a1':a})
def editteacher(request,eid):
    if request.method=='POST':
        name=request.POST['nm']
        email=request.POST['em']
        username=request.POST['uname']
        password=request.POST['psw']
        phone=request.POST['ph']
        subject=request.POST['subj']
        x=Teacher.objects.filter(id=eid).update(Name=name,Email=email,Username=username,Password=password,Phone_no=phone,Subject=subject)
        return redirect(viewteacher)
    else:
             
      a=Teacher.objects.get(id=eid)
      return render(request,'Editteacher.html',{'a1':a})

def viewstudent(request):
    a=Student.objects.all()
    return render(request,'Teacher_view_student.html',{'a1':a})

def editstudents(request,eid):
    if request.method=='POST':
        name=request.POST['nm']
        email=request.POST['em']
        username=request.POST['uname']
        password=request.POST['psw']
        class1=request.POST['cls']
        try:
             gender=request.POST['gend']
        except MultiValueDictKeyError:
            gender='female'

        phone_no=request.POST['ph']
        address=request.POST['ad']
        x=Student.objects.filter(id=eid).update(Name=name,Email=email,Username=username,Password=password,cls=class1,Gender=gender,Phone_no=phone_no,Address=address)
        return redirect(managestudent)
    else:
          a=Student.objects.get(id=eid)
          return render(request,'editstudents.html',{'a1':a})
def deletestudents(request,did):
    x=Student.objects.get(id=did)
    x.delete()
    return redirect(managestudent)
def deleteteacher(request,did):
    x=Teacher.objects.get(id=did)
    x.delete()
    return redirect(viewteacher)
def Homepage(request):
    return render(request,'Homepage.html')
def managestudent(request):
    a=Student.objects.all()
    return render(request,'managestudent.html',{'a1':a})
def studviewteacher(request):
    a=Teacher.objects.all()
    return render(request,'student_view_teacher.html',{'a1':a})


def studprofile(request):
    a=request.session['stud_id']
    stu=Student.objects.filter(id=a)
    return render(request,'studentprofile.html',{'a1':stu})   
def editstudprofile(request):
        a=request.session['stud_id']
        stu=Student.objects.filter(id=a)
        return render(request,'Editstudentprofile.html',{'a1':stu})
def editstudprofile1(request):
    if request.method=='POST':

        name=request.POST['nm']
        email=request.POST['em']
        username=request.POST['uname']
        password=request.POST['psw']
        class1=request.POST['cls']
        try:
             gender=request.POST['gend']
        except MultiValueDictKeyError:
            gender='female'
        phonenumber=request.POST['ph']
        address=request.POST['ad']
        a=request.session['stud_id']

        x=Student.objects.filter(id=a).update(Name=name,Email=email,Username=username,Password=password,cls=class1,Gender=gender,Phone_no=phonenumber,Address=address)
        return redirect(studprofile)
def teacherprofile(request):
    a=request.session['teacher_id']
    teach=Teacher.objects.filter(id=a)
    return render(request,'Teacherprofile.html',{'a1':teach})

def Editteacherprofile(request):
    a=request.session['teacher_id']
    teach=Teacher.objects.filter(id=a)
    return render(request,'EditTeacherprofile.html',{'a1':teach})

def Editteacherprofile1(request):
    if request.method=='POST':
        name=request.POST['nm']
        email=request.POST['em']
        username=request.POST['uname']
        password=request.POST['psw']
        phone=request.POST['ph']
        subject=request.POST['subj']
        a=request.session['teacher_id']
        x=Teacher.objects.filter(id=a).update(Name=name,Email=email,Username=username,Password=password,Phone_no=phone,Subject=subject)
        return redirect(teacherprofile)


    
   

           


 



   

    
