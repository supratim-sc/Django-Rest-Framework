from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TeachersList.as_view()),
    path('<int:pk>', views.TeacherDetails.as_view()),
]