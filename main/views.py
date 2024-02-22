from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View

# Create your views here.


def say_hello(req):
    return HttpResponse("<h1>Hello Fleur</h1>")

# function: UserProfile name: your name, email: your email, phone number: your phone number  
# view function returns a JsonResponse 
# register the view function on a path called profile

def user_profile(req):

    return JsonResponse(
        {
       "name": "Misheck" ,
       "email": "misheck.lukhama@meltwater.org",
       "Phone_number": "0536075543"
    }
    )
    

# write a view function called filter_queries
# the view function should receive query_id through the url
# return a JsonResponse data with the following data id, title, description, status
#and submitted_by
#the id should be the id received through the url

def filter_queries(req,id):
    return JsonResponse(
        {
            "id": id,
            "title": "Wedding Dress",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam",
            "status": "in progress",
            "submitted_by": "Courtney"
        }
    )
     
class QueryView(View):
    queries = [
        {
                "id":1, "title": "Adama declined Val shot"
            },
        {
                "id":1, "title": "Adama declined Val shot"
            }
        ]
    
    def get(self, req):

        return JsonResponse({"result": self.queries})
    
    def post(self,req):
        return JsonResponse({"status": "ok"})