from django.urls import path
from .views import studentsList
 
urlpatterns = [
    path('students-list/', studentsList)
]