from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def user_profile(request):
     profile_data = (
         {
        'Name': 'Misheck Lukhama',
        'email': 'misheck.lukhama@meltwater.org',
        'phone_number': '0536075543',
    }
     )
     return JsonResponse(profile_data)