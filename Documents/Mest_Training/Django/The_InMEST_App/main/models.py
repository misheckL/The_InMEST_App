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
    MEETING_TYPES = (
        ("CLASS_SECTIONS", 'Class Sessions'),
        ("WELLNESS_SESSIONS", 'Well Session'),
        ('GUEST_LECTURE', 'Guest Lecture')
    )
    REPEAT_FREQUENCY = (
        ("DAILY", 'Daily'),
        ("WEEKLY", 'Weekly'),
        ('MONTHLY', 'Monthly')
    )
    title = models.CharField(max_length = 255)
    description = models.TextField(default ="N/A", blank=True, null=True)
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField()
    is_repeated = models.BooleanField(default = False)
    repeat_frequency = models.CharField(max_length=20, choices=REPEAT_FREQUENCY, default='DAILY')
    meeting_types = models.CharField(max_length=20, choices=MEETING_TYPES, default='CLASS SESSIONS')
    is_active = models.BooleanField(default = False)
    organizer = models.CharField(max_length = 255)
    cohort = models.ForeignKey(Cohort, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.SET_NULL, blank=True, null=True, related_name="course_class_schedule")
    facilitator = models.ForeignKey(IMUser, on_delete = models.SET_NULL, blank=True, null=True, related_name="facilitator_class_schedule")
    venue = models.CharField(max_length = 255)
    date_created = models.DateTimeField(auto_now_add = True, blank = True, null = True)
    date_modified = models.DateTimeField(auto_now = True, blank = True, null=True)
    
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
    
    
# class ResolutionStatus(models.Model):
#     resolution_status = models.CharField(max_length = 225, unique = True)
    
#     def __str__(self):
#         return self.resolution_status
    
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

    title = models.CharField(max_length = 255)
    description = models.TextField(default ="N/A", blank=True, null=True)
    submitted_by = models.ForeignKey(IMUser, on_delete = models.CASCADE)
    assigned_to = models.ForeignKey(IMUser, on_delete = models.CASCADE, related_name = 'assigned')
    # resolution_status = models.ForeignKey(ResolutionStatus, on_delete = models.CASCADE)
    resolution_status = models.CharField(max_length = 50, choices = RESOLUTION_STATUS_CHOICES, default=PENDING)
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
    