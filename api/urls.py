from django.urls import path, include

urlpatterns = [
    path('students/', include('students.urls')),
    path('employees/', include('employee.urls')),
    path('library/', include('library.urls')),
]