from django.db import models
import datetime
from users.models import Cohort, IMUser

# Create your models here.

class Course(models.Model):
    name=models.CharField(max_length=1000)
    description = models.TextField(default ="N/A", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank =True, null = True)
    date_modified = models.DateTimeField(auto_now=True, blank =True, null = True)
    
    def __str__(self):
        return f"{self.name}"
        
    
class ClassSchedule(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(default ="N/A", blank=True, null=True)
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField()
    is_repeated = models.BooleanField(default = False)
    repeat_frequency = models.IntegerField()
    is_active = models.BooleanField(default = False)
    organizer = models.CharField(max_length = 255)
    cohort = models.ForeignKey(Cohort, on_delete = models.CASCADE)
    venue = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.title
    
    
class ClassAttendance(models.Model):
    class_schedule = models.ForeignKey(ClassSchedule, on_delete = models.CASCADE)
    attendee = models.ForeignKey(IMUser, on_delete = models.CASCADE, related_name = "attendee_members")
    is_present = models.BooleanField(default = False)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(IMUser, on_delete = models.CASCADE, related_name='authored_attendance')
    
    # def __str__(self):
    #     return f"(self.member.attendee) in (self.title)"
    
    
class ResolutionStatus(models.Model):
    resolution_status = models.CharField(max_length = 225, unique = True)
    
    def __str__(self):
        return self.resolution_status
    
class Query(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(default ="N/A", blank=True, null=True)
    submitted_by = models.ForeignKey(IMUser, on_delete = models.CASCADE)
    assigned_to = models.ForeignKey(IMUser, on_delete = models.CASCADE, related_name = 'assigned')
    resolution_status = models.ForeignKey(ResolutionStatus, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(IMUser, on_delete = models.CASCADE, related_name = 'author')
    
    def __str__(self):
        return self.title
    
class QueryComment(models.Model):
    query = models.ForeignKey(Query, on_delete = models.CASCADE)
    comment = models.TextField(default ="N/A", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(IMUser, on_delete = models.CASCADE)
    