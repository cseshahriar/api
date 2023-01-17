from django.urls import path
from api.views import student_detail

urlpatterns = [
    path('<int:pk>/', student_detail, name='student_detail'),
]
