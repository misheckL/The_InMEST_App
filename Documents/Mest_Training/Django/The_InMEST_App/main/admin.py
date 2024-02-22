from django.contrib import admin
from .models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=("name", "date_created", "date_modified")
    
class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "start_date_and_time", "end_date_and_time", "is_repeated", "repeat_frequency", "meeting_types","is_active", "organizer", "cohort", "course","facilitator","venue", "date_created", "date_modified")
    
class ClassAttendanceAdmin(admin.ModelAdmin):
    list_display = ("class_schedule", "attendee", "is_present", "date_created", "date_modified", "author")
    
# class ResolutionStatusAdmin(admin.ModelAdmin):
#     list_display=("resolution_status",)

class QueryAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "submitted_by", "assigned_to", "resolution_status", "date_created", "date_modified", "author")
    
class QueryCommentAdmin(admin.ModelAdmin):
    list_display = ("query", "comment", "date_created", "date_modified", "author")


admin.site.register(Course, CourseAdmin)
admin.site.register(ClassSchedule, ClassScheduleAdmin)
admin.site.register(ClassAttendance, ClassAttendanceAdmin)
# admin.site.register(ResolutionStatus, ResolutionStatusAdmin)
admin.site.register(Query, QueryAdmin)
admin.site.register(QueryComment, QueryCommentAdmin)