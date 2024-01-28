from django.urls import path

from digital_diary.diary.views import (
    courses,
    lessons,
    marks,
    programs,
    students,
    subjects,
    teachers,
)

urlpatterns = [
    path('courses/', courses.CourseListAPIView.as_view(), name='course-list'),
    path('courses/new/', courses.CourseCreateAPIView.as_view(), name='course-create'),
    path('courses/<int:pk>/', courses.CourseRetrieveUpdateDestroyAPIView.as_view(), name='course'),
    path('students/', students.StudentListAPIView.as_view(), name='student-list'),
    path('students/new/', students.StudentCreateAPIView.as_view(), name='student-create'),
    path('students/<str:username>/', students.StudentRetrieveUpdateDestroyAPIView.as_view(),
         name='student'),
    path('teachers/', teachers.TeacherListAPIView.as_view(), name='teacher-list'),
    path('teachers/new/', teachers.TeacherCreateAPIView.as_view(), name='teacher-create'),
    path('teachers/<str:username>/', teachers.TeacherRetrieveUpdateDestroyAPIView.as_view(),
         name='teacher'),
    path('subjects/', subjects.SubjectListAPIView.as_view(), name='subject-list'),
    path('subjects/new/', subjects.SubjectCreateAPIView.as_view(), name='subject-create'),
    path('subjects/<int:pk>/', subjects.SubjectRetrieveUpdateDestroyAPIView.as_view(),
         name='subject'),
    path('programs/', programs.ProgramListAPIView.as_view(), name='program-list'),
    path('programs/new/', programs.ProgramCreateAPIView.as_view(), name='program-create'),
    path('programs/<int:pk>/', programs.ProgramRetrieveUpdateDestroyAPIView.as_view(),
         name='program'),
    path('lessons/', lessons.LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/new/', lessons.LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/<int:pk>/', lessons.LessonRetrieveUpdateDestroyAPIView.as_view(), name='lesson'),
    path('marks/', marks.MarkAPIView.as_view(), name='marks'),
    path('marks/new/', marks.MarkCreateAPIView.as_view(), name='mark-create'),
    path('marks/<int:pk>/', marks.MarkRetrieveUpdateDestroyAPIView.as_view(), name='mark'),
]
