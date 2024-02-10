from django.contrib import admin
from .models import *
from .models import IMUser, Cohort, CohortMember

@admin.register(IMUser)
class IMUserAdmin(admin.ModelAdmin):
    list_display = ['FIRST_NAME', 'LAST_NAME', 'IS_ACTIVE', 'USER_TYPE', 'DATE_CREATED']

@admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):
    list_display = ['NAME', 'YEAR', 'START_DATE', 'END_DATE', 'IS_ACTIVE', 'AUTHOR', 'DATE_CREATED', 'DATE_MODIFIED']

@admin.register(CohortMember)
class CohortMemberAdmin(admin.ModelAdmin):
    list_display = ['MEMBER', 'COHORT', 'IS_ACTIVE', 'DATE_CREATED', 'DATE_MODIFIED', 'AUTHOR']
