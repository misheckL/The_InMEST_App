from django.db import models
from .models import * 
from django.contrib import admin
from django.db.models import TextChoices
from users.models import IMUser  # Import the IMUser model
from users.models import Cohort  # Import the Cohort model



# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=2000)
    description = models.TextField(default='N/A', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}"
    
class ClassSchedule(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField()
    is_repeated = models.BooleanField(default=False)
    repeat_frequency = models.IntegerField(null=True, blank=True)  # Define appropriate choices if needed
    is_active = models.BooleanField(default=True)
    organizer = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='organized_classes')
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='class_schedules')
    venue = models.CharField(max_length=255)

    def __str__(self):
        return self.title

from django.db import models
from users.models import IMUser  # Import the IMUser model
from .models import ClassSchedule  # Import the ClassSchedule model

class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE, related_name='attendances')
    attendee = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='attended_classes')
    is_present = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='created_attendances')

    def __str__(self):
        return f"{self.attendee} - {self.class_schedule}"

from django.db import models
from users.models import IMUser  # Import the IMUser model

class Query(models.Model):
    PENDING = 'PENDING'
    IN_PROGRESS = 'IN_PROGRESS'
    DECLINED = 'DECLINED'
    RESOLVED = 'RESOLVED'

    RESOLUTION_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (DECLINED, 'Declined'),
        (RESOLVED, 'Resolved'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    submitted_by = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='submitted_queries')
    assigned_to = models.ForeignKey(IMUser, on_delete=models.CASCADE, null=True, blank=True, related_name='assigned_queries')
    resolution_status = models.CharField(max_length=30, choices=RESOLUTION_STATUS_CHOICES, default=PENDING)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_queries')

    def __str__(self):
        return self.title

class QueryComment(models.Model):
    query = models.ForeignKey(Query, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='written_comments')

    def __str__(self):
        return f"{self.author} - {self.query}"

