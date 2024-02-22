from django.contrib import admin
from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=("first_name", "last_name", "is_active", "user_type", "date_created")
    
# class UserTypeAdmin(admin.ModelAdmin):
#     list_display=("name",)
    
class CohortAdmin(admin.ModelAdmin):
    list_display=("name", "description", "year", "start_date", "end_date", "is_active", "date_created", "date_modified", "author")
    
class CohorMemberAdmin(admin.ModelAdmin):
    list_display=("cohort", "members", "is_active", "date_created", "date_modified")



# admin.site.register(UserType, UserTypeAdmin)
admin.site.register(IMUser, UserAdmin)
admin.site.register(Cohort, CohortAdmin)
admin.site.register(CohorMember, CohorMemberAdmin)

