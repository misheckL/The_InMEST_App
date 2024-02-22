# InMEST - Student Class Attendance Tracking System
InMEST is a student class attendance tracking system built in Django. It facilitates the monitoring of student attendance, course management, and integrates Django REST Framework for API functionalities.

## Installation
1. Install Django:
   python -m pip install Django
**Create a virtual environment (optional but recommended):**
python -m venv my_env
source my_env/Scripts/activate

**Create Main and Users apps:**
python3 manage.py startapp Main
python3 manage.py startapp Users

**Run database migrations:**
python manage.py makemigrations
python manage.py migrate

**Run the development server:**
python3 manage.py runserver

**Access the Django shell for query requests:**
python3 manage.py shell
Django React Framework
For additional functionality and API support, Django REST Framework is integrated:

**Install Django REST Framework:**
python -m pip install djangorestframework

**Install Markdown and Django Filter (optional but useful for API development):**
pip install markdown
pip install django-filter

**Query Requests in Django Shell**
In the Django shell, you can run various query requests, for example:
*List all courses:*
from Main.models import Course
Course.objects.all()
