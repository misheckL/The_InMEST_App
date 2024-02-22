from django.contrib import admin
from .models import *
from.models import *
from .models import ClassSchedule
from django.contrib import admin
from .models import ClassAttendance
from .models import Query




# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display=("name", "date_created", "date_modified")
admin.site.register(Course, CourseAdmin)

@admin.register(ClassSchedule)
class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'start_date_and_time', 'end_date_and_time', 'is_repeated', 'repeat_frequency', 'is_active', 'organizer', 'cohort', 'venue')

@admin.register(ClassAttendance)
class ClassAttendanceAdmin(admin.ModelAdmin):
    list_display = ('class_schedule', 'attendee', 'is_present', 'date_created', 'date_modified', 'author')

@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'submitted_by', 'assigned_to', 'resolution_status', 'date_created', 'date_modified', 'author')

from django.contrib import admin
from .models import QueryComment

@admin.register(QueryComment)
class QueryCommentAdmin(admin.ModelAdmin):
    list_display = ('query', 'comment', 'date_created', 'date_modified', 'author')
