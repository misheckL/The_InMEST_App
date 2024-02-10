from django.db import models
from django.utils import timezone

# Define the IMUser model
class IMUser(models.Model):
    FIRST_NAME = models.CharField(max_length=50)
    LAST_NAME = models.CharField(max_length=50)
    IS_ACTIVE = models.BooleanField(default=True)
    USER_TYPE_CHOICES = [{'choice', 'SELECT USER'},
        ('EIT', 'EIT'),
        ('Teaching Fellow', 'TEACHING FELLOW'),
        ('Admin Staff', 'ADMIN STAFF'),
        ('Admin', 'ADMIN')
    ]
    USER_TYPE = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)
    DATE_CREATED = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.FIRST_NAME} {self.LAST_NAME}"

# Define the Cohort model
class Cohort(models.Model):
    NAME = models.CharField(max_length=100)
    DESCRIPTION = models.TextField()
    YEAR = models.IntegerField()
    START_DATE = models.DateField()
    END_DATE = models.DateField()
    IS_ACTIVE = models.BooleanField(default=True)
    DATE_CREATED = models.DateTimeField(auto_now_add=True)
    DATE_MODIFIED = models.DateTimeField(auto_now=True)
    AUTHOR = models.ForeignKey(IMUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.NAME

# Define the CohortMember model
class CohortMember(models.Model):
    COHORT = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    MEMBER = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohort_members')
    IS_ACTIVE = models.BooleanField(default=True)
    DATE_CREATED = models.DateTimeField(auto_now_add=True)
    DATE_MODIFIED = models.DateTimeField(auto_now=True)
    AUTHOR = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='authored_cohort_members')

    def __str__(self):
        return f"{self.MEMBER.FIRST_NAME} {self.MEMBER.LAST_NAME} - {self.COHORT.NAME}"
