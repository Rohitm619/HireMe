# HireMe
Online Job Portal

Start this Django webapp locally on your machine. (Make sure you installed django on your machine before following the steps.)

1. Clone the Repository -
```git clone https://github.com/Rohitm619/HireMe.git```

2. Install your requirements -
```pip install -r requirements.txt```

3. Check into the project directory where ```manage.py``` file is located.

4. Open the command prompt in the directory (step 3), and run the command ```python manage.py runserver```

5. Server should be started. Now open the URL provided in command prompt in browser.

----------------------------------------------------------------------

Features of HireMe -

- Jobseeker has to register on the website before login. Without it, he/she can't apply for the job.
- Jobseeker has to provide ```Name, Contact Number, Email, Gender, Profile Photo``` and can login through the email and password that he has provided during registration.
- Recruiter also has to register on the website for posting jobs.
- Recruiter has to provide ```Name, Contact Number, Email, Gender, Profile Photo, Company Name```.
- ```Jobseeker/Recruiter can edit his name, contact number, gender, profile photo later```.
- Once recruiter registered on the website, he has to wait till admin allow it. After allowing, he can login through the email and password that he has provided during registration.
- Admin is the website owner, who can handle all the recruiters and jobseekers.
- Admin can delete the recruiter and also user. Admin can refuse the recruiter request for signing up.
- Recruiter has an option to add new jobrole, he has to provide ```Job Title, Start Date, End Date, Salary, Company Logo, Required Experience, Required Skills, Job Location(s), Description```.
- Recruiter can edit/delete the existing job details later.
- Once Jobseeker logged in, he/she can see all the details of the job and can apply to all the jobs posted by recruiter.


Thank You!
