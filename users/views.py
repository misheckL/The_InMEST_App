from django.shortcuts import render

from users.models import IMUser

# Create your views here.
def signUp(request):
    username = request.POST["username"]
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    phone_number = request.POST["phone_number"]
    password = request.POST["password"]
    
    new_user = IMUser.objects.create(
        username = username,
        first_name = first_name,
        last_name = last_name,
        phone_number = phone_number
    )
    new_user.set_password(password)
    new_user.save()
