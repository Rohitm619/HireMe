"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from job.views import *     #To use functions defined in views.py


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('adminrohit/', admin.site.urls),
    path('', index, name="index"),
    path('admin_login', admin_login, name="admin_login"),
    path('user_login', user_login, name="user_login"),
    path('recruiter_login', recruiter_login, name="recruiter_login"),
    path('user_signup', user_signup, name="user_signup"),
    path('recruiter_signup', recruiter_signup, name="recruiter_signup"),
    path('user_home', user_home, name="user_home"),
    path('admin_home', admin_home, name="admin_home"),
    path('Logout', Logout, name="Logout"),
    path('recruiter_home', recruiter_home, name="recruiter_home"),
    
    path('view_users', view_users, name="view_users"),
    path('delete_user/<int:pid>', delete_user, name="delete_user"),
    path('recruiter_pending', recruiter_pending, name="recruiter_pending"),
    path('about_us', about_us, name="about_us"),
    path('change_status/<int:pid>', change_status, name="change_status"),
    path('recruiter_accepted', recruiter_accepted, name="recruiter_accepted"),
    path('recruiter_rejected', recruiter_rejected, name="recruiter_rejected"),
    path('recruiter_all', recruiter_all, name="recruiter_all"),
    path('delete_recruiter/<int:pid>', delete_recruiter, name="delete_recruiter"),
    path('changepasswordadmin', changepasswordadmin, name="changepasswordadmin"),
    path('changepassworduser', changepassworduser, name="changepassworduser"),
    path('changepasswordrecruiter', changepasswordrecruiter, name="changepasswordrecruiter"),
    path('add_job', add_job, name="add_job"),
    path('job_list', job_list, name="job_list"),
    path('edit_jobdetail/<int:pid>', edit_jobdetail, name="edit_jobdetail"),
    path('change_companylogo/<int:pid>', change_companylogo, name="change_companylogo"),
    path('view_jobs', view_jobs, name="view_jobs"),
    path('latest_jobs', latest_jobs, name="latest_jobs"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
