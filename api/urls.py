from django.urls import path

from .views import  StudentListAPIView, StudentRetrieveAPIView, BookListAPIView, BookRetrieveAPIView


urlpatterns = [
    path('students/', StudentListAPIView.as_view()),
    path('students/<int:pk>/', StudentListAPIView.as_view()),
    path('student/course/<int:student_id>', StudentRetrieveAPIView.as_view()),
    path('book/',BookListAPIView.as_view()),
    path('book/<int:pk>', BookListAPIView.as_view()),
    path('student/genre/<int:pk>', BookRetrieveAPIView.as_view()),

]

url = ['https://x.com/wallpiics/status/2052026000175673656']

