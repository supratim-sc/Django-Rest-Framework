from django.urls import path, include

urlpatterns = [
    path('students/', include('students.urls')),
    path('employees/', include('employee.urls')),
    path('library/', include('library.urls')),
    path('teachers/', include('teachers.urls')),
    path('movies/', include('movies.urls')),
    path('blogs/', include('blogs.urls')),
]