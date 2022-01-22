from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date


# Create your views here.
def index(request):
    return render(request,'index.html')

def about_us(request):
    return render(request,'about_us.html')

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {"error": error}
    return render(request,'admin_login.html',d)

def user_login(request):
    error=""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)

        if user:
            try:
                user1 = StudentUser.objects.get(user=user)
                if user1.type == "student":
                    login(request,user)
                    error="no"
                else:   
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"

    d = {'error':error}
    return render(request,'user_login.html', d)

def recruiter_login(request):
    error=""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)

        if user:
            try:
                user1 = Recruiter.objects.get(user=user)
                if user1.type == "recruiter" and user1.status!="pending":
                    login(request,user)
                    error="no"
                else:   
                    error="not"
            except:
                error="yes"
        else:
            error="yes"

    d = {'error':error}
    return render(request,'recruiter_login.html',d)


def user_signup(request):
    error = ""
    if (request.method == 'POST'):
        f = request.POST['fname']
        l = request.POST['lname']
        con = request.POST['contact']
        e = request.POST['email']
        gen = request.POST['gender']
        p = request.POST['pwd']
        i = request.FILES['image']

        try:
            user = User.objects.create_user(first_name=f, username=e, email=e, last_name=l, password=p)
            StudentUser.objects.create(user=user, mobile=con, image=i, gender=gen, type="student")
            error = "no"
        except:
            error = "yes"


    d = {'error' : error}
    return render(request,'user_signup.html', d)

def recruiter_signup(request):
    error = ""
    if (request.method == 'POST'):
        f = request.POST['fname']
        l = request.POST['lname']
        con = request.POST['contact']
        e = request.POST['email']
        gen = request.POST['gender']
        p = request.POST['pwd']
        i = request.FILES['image']
        company = request.POST['company']

        try:
            user = User.objects.create_user(first_name=f, username=e, email=e, last_name=l, password=p)
            Recruiter.objects.create(user=user, mobile=con, image=i, gender=gen, company=company, type="recruiter", status="pending")
            error = "no"
        except:
            error = "yes"

    d = {'error' : error}
    return render(request,'recruiter_signup.html',d)

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')

    user = request.user
    student = StudentUser.objects.get(user=user)

    error = ""
    if (request.method == 'POST'):
        f = request.POST['fname']
        l = request.POST['lname']
        con = request.POST['contact']
        gen = request.POST['gender']
        

        student.user.first_name = f
        student.user.last_name = l
        student.mobile = con
        student.gender = gen
        try:
            student.save()
            student.user.save()
            error = "no"
        except:
            error = "yes"

        try:
            i = request.FILES['image']
            student.image = i
            student.save()
            error = "no"
        except:
            pass

    d = {'student':student, "error":error}
    return render(request,'user_home.html',d)

def Logout(request):
    logout(request)
    return redirect('index')

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')

    user = request.user
    recruiter = Recruiter.objects.get(user=user)

    error = ""
    if (request.method == 'POST'):
        f = request.POST['fname']
        l = request.POST['lname']
        con = request.POST['contact']
        gen = request.POST['gender']
        

        recruiter.user.first_name = f
        recruiter.user.last_name = l
        recruiter.mobile = con
        recruiter.gender = gen
        try:
            recruiter.save()
            recruiter.user.save()
            error = "no"
        except:
            error = "yes"

        try:
            i = request.FILES['image']
            recruiter.image = i
            recruiter.save()
            error = "no"
        except:
            pass

    d = {'recruiter':recruiter, "error":error}
    return render(request,'recruiter_home.html',d)


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')

def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = StudentUser.objects.all()
    d = {'data':data}
    return render(request,'view_users.html',d)

def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status="pending")
    d = {'data':data}
    return render(request,'recruiter_pending.html',d)


def delete_user(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = User.objects.get(id=pid)
    student.delete()
    return redirect('view_users')

def change_status(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    recruiter = Recruiter.objects.get(id=pid)
    if request.method=="POST":
        s = request.POST['status']
        recruiter.status = s
        try:
            recruiter.save()
            error="no"
        except:
            error="yes"
    d = {'recruiter':recruiter, 'error':error}
    return render(request,'change_status.html',d)


def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status="Accept")
    d = {'data':data}
    return render(request,'recruiter_accepted.html',d)

def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status="Reject")
    d = {'data':data}
    return render(request,'recruiter_rejected.html',d)

def recruiter_all(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.all()
    d = {'data':data}
    return render(request,'recruiter_all.html',d)

def delete_recruiter(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiter = User.objects.get(id=pid)
    recruiter.delete()
    return redirect('recruiter_all')

def changepasswordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method=="POST":
        c = request.POST['currentpassword'] #currentpass
        n = request.POST['newpassword'] #newpass
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):     #convering to hash form by check_password function
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'change_passwordadmin.html',d)


def changepassworduser(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    if request.method=="POST":
        c = request.POST['currentpassword'] #currentpass
        n = request.POST['newpassword'] #newpass
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):     #convering to hash form by check_password function
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'change_passworduser.html',d)

def changepasswordrecruiter(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    if request.method=="POST":
        c = request.POST['currentpassword'] #currentpass
        n = request.POST['newpassword'] #newpass
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):     #convering to hash form by check_password function
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'change_passwordrecruiter.html',d)

def add_job(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    if (request.method == 'POST'):
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        l = request.FILES['logo']
        exp = request.POST['experience']
        loc = request.POST['location']
        skills = request.POST['skills']
        des = request.POST['description']
        user = request.user
        recruiter = Recruiter.objects.get(user=user)
        try:
            Job.objects.create(recruiter=recruiter, start_date=sd, end_date=ed, title=jt, salary=sal, image=l, description=des, experience=exp, location=loc, skills=skills, creationdate=date.today())
            error = "no"
        except:
            error = "yes"
    d = {'error' : error}
    return render(request,'add_job.html',d)

def job_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    job = Job.objects.filter(recruiter=recruiter)
    d = {'job':job}
    return render(request,'job_list.html',d)

def edit_jobdetail(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    job = Job.objects.get(id=pid)
    if (request.method == 'POST'):
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        exp = request.POST['experience']
        loc = request.POST['location']
        skills = request.POST['skills']
        des = request.POST['description']
        
        job.title = jt
        job.salary = sal
        job.experience = exp
        job.location = loc
        job.skills = skills
        job.description = des

        try:
            job.save()
            error = "no"
        except:
            error = "yes"
        
        if (sd):
            try:
                job.start_date = sd
                job.save()
            except:
                pass


        if (ed):
            try:
                job.end_date = ed
                job.save()
            except:
                pass

    d = {'error' : error, 'job':job}
    print(error)
    return render(request,'edit_jobdetail.html',d)

def change_companylogo(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    job = Job.objects.get(id=pid)
    if (request.method == 'POST'):
        
        cl = request.FILES['logo']
        
        
        job.image = cl

        try:
            job.save()
            error="no"
        except:
            error="yes"

    d = {'error' : error, 'job':job}
    return render(request,'change_companylogo.html',d)

def view_jobs(request):
    if not request.user.is_authenticated:
        return redirect('user_login')

    std = request.user
    student = StudentUser.objects.get(user=std)

    job = Job.objects.all()
    rec = Recruiter.objects.all()
    d = {'job':job, 'student':student, 'rec':rec}
    return render(request,'view_jobs.html',d)

def latest_jobs(request):
    job = Job.objects.all()
    rec = Recruiter.objects.all()
    d = {'job':job, 'rec':rec}
    return render(request,'latest_jobs.html',d)