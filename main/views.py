from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from django.views import View

# Create your views here.

def json_response(request):
    print("Hi Lucky")
    
def http_response(request):
    print("")
    
def say_hello(req):
    return HttpResponse("<h1>Hello Misheck below are your details</h1>"),


#Write a view function User_profiles
#Return should be write a json function
#Name: your name, emaila; your email, phone_number: your phone number
#register the view function on the path called profile

def user_profile(request):
     profile_data = (
         {
        'Name': 'Misheck Lukhama',
        'email': 'misheck.lukhama@meltwater.org',
        'phone_number': '0536075543',
    }
     )
     return JsonResponse(profile_data)
 #write a view function called filter_queries
 # the view function should receive query_Id through the url
 #Return a JsonResponse data with the following
 #data: id, title, description, ststus, and submitted_by
 #the id should be the id receive through the url
 
def filter_queries(request, query_id):
     data = {
        'id': "1",
        'title': "Up with Misheck",
        'description': "This is a show that showcases Misheck's Lifestyle",
        'status': "PENDING",
        'submitted_by': "Misheck Lukhama",
    }
     return JsonResponse({'data': data})

class QueryView(View):
    queries = [
            {"id": 1, "title": "Adama delinced val shots"},
            {"id": 2, "title": "samson delinced val shots"},
        ]
    def get(self, request):
        return JsonResponse({"result": self.queries})
    
    def post(self, request):
        return JsonResponse({"status": "ok"})
    
    ##The "self" aurgument is applied to the class-based in this case the QueryView,
    #The request makes available the input from the user
    #The self helps us have access to the instance of the class