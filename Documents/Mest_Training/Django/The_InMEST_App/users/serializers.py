from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    # username = serializers.CharField()
    email = serializers.CharField()
    
class CohortSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    year = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    # is_active = serializers.BooleanField()
    author = UserSerializer(many=False)
    
class CohorMemberSerializer(UserSerializer, serializers.Serializer):
    members = UserSerializer()
