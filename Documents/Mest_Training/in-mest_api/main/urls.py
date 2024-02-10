from django import views
from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path("say_hello/", say_hello),
    path("user_profile/", user_profile, name='user_profile'),
    path('filter_queries/<int:query_id>/', filter_queries),
    path("queries/", QueryView.as_view(), name="query-view")
]
