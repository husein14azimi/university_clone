from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseList.as_view()),
    path('courses/<int:pk>/', views.CourseDetail.as_view()),

    path('course-steps/', views.CourseStepList.as_view()),
    path('course-steps/<int:pk>/', views.CourseDetail.as_view()),

    path('students/', views.StudentList.as_view()),
    path('students/<int:pk>/', views.StudentDetail.as_view()),

    path('course-student-relationships/', views.CourseStudentRelationshipList.as_view()),
    path('course-student-relationships/<int:pk>/', views.CourseStudentRelationshipDetail.as_view()),
]