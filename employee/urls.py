from django.urls import path, include
from .views import EmployeeList, EmployeeDetails

urlpatterns = [
    path('', EmployeeList.as_view()),
    path('<int:pk>/', EmployeeDetails.as_view()),
]