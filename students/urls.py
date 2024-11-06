from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.studentsList),
    path('<int:pk>/', views.studentDetails)
]