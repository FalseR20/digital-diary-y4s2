from django.urls import path

from . import views

urlpatterns = [
    path('courses/', views.CourseListAPIView.as_view(), name='course-list'),
    path('courses/new/', views.CourseCreateAPIView.as_view(), name='course-create'),
    path('courses/<int:pk>/', views.CourseRetrieveUpdateDestroyAPIView.as_view(), name='course'),
    path('students/', views.StudentListAPIView.as_view(), name='student-list'),
    path('students/new/', views.StudentCreateAPIView.as_view(), name='student-create'),
    path('students/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view(),
         name='student'),
    path('teachers/', views.TeacherListAPIView.as_view(), name='teacher-list'),
    path('teachers/new/', views.TeacherCreateAPIView.as_view(), name='teacher-create'),
    path('teachers/<int:pk>/', views.TeacherRetrieveUpdateDestroyAPIView.as_view(),
         name='teacher'),
    path('subjects/', views.SubjectListAPIView.as_view(), name='subject-list'),
    path('subjects/new/', views.SubjectCreateAPIView.as_view(), name='subject-create'),
    path('subjects/<int:pk>/', views.SubjectRetrieveUpdateDestroyAPIView.as_view(),
         name='subject'),
    path('programs/', views.ProgramListAPIView.as_view(), name='program-list'),
    path('programs/new/', views.ProgramCreateAPIView.as_view(), name='program-create'),
    path('programs/<int:pk>/', views.ProgramRetrieveUpdateDestroyAPIView.as_view(),
         name='program'),
    path('lessons/', views.LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/new/', views.LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/<int:pk>/', views.LessonRetrieveUpdateDestroyAPIView.as_view(), name='lesson'),
    path('marks/', views.MarkAPIView.as_view(), name='marks'),
    path('marks/new/', views.MarkCreateAPIView.as_view(), name='mark-create'),
    path('marks/<int:pk>/', views.MarkRetrieveUpdateDestroyAPIView.as_view(), name='mark'),
]
