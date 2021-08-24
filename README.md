# django-job-bord
An app that lets you post a job or search and apply a job

# Demo
## https://djangojobboard.herokuapp.com/



# Usage
It's best to install Python projects in a Virtual Environment. Once you have set up a Virtual Environment, clone this project
 ```
 git clone https://github.com/M0hamedEmad/django-job-bord.git
 ```
 then cd to file and Run
 ```
pip install -r requirements.txt #install required packages
python manage.py migrate # run first migration
python manage.py runserver # run the server
 ```
 then open in your browser http://127.0.0.1:8000/
 
 # Make a Superuser
 Run
 ```
 python manage.py createsuperuser
 ```
 then write a username, email, password 
 go to http://127.0.0.1:8000/admin  a django admin
 or http://127.0.0.1:8000/dashboard/jobs  a dashboard for admin and editors
 


# Features
 * Add job
 * Apply job
 * Activate or inactive the poll
 * search and filter for all jobs


