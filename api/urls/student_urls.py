from django.urls import path
from api.views import student_detail, student_list

urlpatterns = [
    path('', student_list, name='student_list'),
    path('<int:pk>/', student_detail, name='student_detail'),
]
