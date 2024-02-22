from rest_framework import serializers
from main.models import ClassSchedule, Query
from users.models import IMUser, Cohort
from users.serializers import CohortSerializer, UserSerializer

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    date_created = serializers.DateTimeField()
    
class ClassScheduleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    start_date_and_time = serializers.DateTimeField()
    end_date_and_time = serializers.DateTimeField()
    is_repeated = serializers.BooleanField()
    repeat_frequency = serializers.CharField()
    # is_active = serializers.BooleanField()
    organizer = UserSerializer(many=False)
    meeting_type = serializers.CharField()
    facilitator = UserSerializer()
    course = CourseSerializer(many=False)
    cohort = CohortSerializer(many=False)
    venue = serializers.CharField()
    
class ClassAttendance(serializers.Serializer):
    class_schedule = ClassScheduleSerializer(ClassSchedule)
    attendee = UserSerializer(IMUser)
    is_present = serializers.CharField()
    author = UserSerializer(IMUser)
    
class QuerySerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    submitted_by = UserSerializer(IMUser)
    assigned_to = UserSerializer(IMUser)
    resolution_status = serializers.CharField()
    author = UserSerializer(IMUser)
    
class QueryCommentSerializer(serializers.Serializer):
    query = QuerySerializer(Query)
    comment = serializers.CharField()
    author = UserSerializer()
    
