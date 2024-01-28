from rest_framework import generics

from . import serializers, models


# Courses

# noinspection DuplicatedCode
class CourseListAPIView(generics.ListAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class CourseCreateAPIView(generics.CreateAPIView):
    queryset = models.Course.objects
    serializer_class = serializers.CourseSerializer


class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


# Students

class StudentListAPIView(generics.ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


# noinspection DuplicatedCode
class StudentCreateAPIView(generics.CreateAPIView):
    queryset = models.Student.objects
    serializer_class = serializers.StudentSerializer

    def perform_create(self, serializer):
        username = serializer.validated_data.pop('user_username')
        user = models.User.objects.get(username=username, )
        serializer.save(user=user)


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

    def perform_update(self, serializer):
        kwargs = {}
        if username := serializer.validated_data.get('user_username'):
            user = models.User.objects.get(username=username)
            kwargs["user"] = user
        serializer.save(**kwargs)


# Teachers

# noinspection DuplicatedCode
class TeacherListAPIView(generics.ListAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer


# noinspection DuplicatedCode
class TeacherCreateAPIView(generics.CreateAPIView):
    queryset = models.Teacher.objects
    serializer_class = serializers.TeacherSerializer

    def perform_create(self, serializer):
        username = serializer.validated_data.pop('user_username')
        user = models.User.objects.get(username=username, )
        serializer.save(user=user)


class TeacherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer

    def perform_update(self, serializer):
        kwargs = {}
        if username := serializer.validated_data.get('user_username'):
            user = models.User.objects.get(username=username)
            kwargs["user"] = user
        serializer.save(**kwargs)


# Subjects


class SubjectListAPIView(generics.ListAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


class SubjectCreateAPIView(generics.CreateAPIView):
    queryset = models.Subject.objects
    serializer_class = serializers.SubjectSerializer


class SubjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


# Programs

class ProgramListAPIView(generics.ListAPIView):
    queryset = models.Program.objects.all()
    serializer_class = serializers.ProgramSerializer


class ProgramCreateAPIView(generics.CreateAPIView):
    queryset = models.Program.objects
    serializer_class = serializers.ProgramSerializer

    def perform_create(self, serializer):
        course_id = serializer.validated_data.pop('course_id')
        course = models.Course.objects.get(pk=course_id)
        subject_id = serializer.validated_data.pop('subject_id')
        subject = models.Subject.objects.get(pk=subject_id)
        teacher_username = serializer.validated_data.pop('teacher_username')
        teacher = models.Teacher.objects.get(user__username=teacher_username)
        serializer.save(course=course, subject=subject, teacher=teacher)


class ProgramRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Program.objects.all()
    serializer_class = serializers.ProgramSerializer

    def perform_update(self, serializer):
        kwargs = {}
        if course_id := serializer.validated_data.get('course_id'):
            course = models.Course.objects.get(pk=course_id)
            kwargs["course"] = course
        if subject_id := serializer.validated_data.get('subject_id'):
            subject = models.Subject.objects.get(pk=subject_id)
            kwargs["subject"] = subject
        if teacher_username := serializer.validated_data.get('teacher_username'):
            teacher = models.Teacher.objects.get(user__username=teacher_username)
            kwargs["teacher"] = teacher
        serializer.save(**kwargs)


# Lessons

class LessonListAPIView(generics.ListAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer

    def perform_create(self, serializer):
        program_id = serializer.validated_data.pop('program_id')
        program = models.Program.objects.get(pk=program_id)
        serializer.save(program=program)


class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Lesson.objects
    serializer_class = serializers.LessonSerializer

    def perform_update(self, serializer):
        kwargs = {}
        if program_id := serializer.validated_data.get('program_id'):
            program = models.Program.objects.get(pk=program_id)
            kwargs["program"] = program
        serializer.save(**kwargs)


# Marks


class MarkAPIView(generics.ListAPIView):
    queryset = models.Mark.objects.all()
    serializer_class = serializers.MarkSerializer


class MarkCreateAPIView(generics.CreateAPIView):
    queryset = models.Mark.objects
    serializer_class = serializers.MarkSerializer

    def perform_create(self, serializer):
        lesson_id = serializer.validated_data.pop('lesson_id')
        lesson = models.Lesson.objects.get(pk=lesson_id)
        student_username = serializer.validated_data.pop('student_username')
        student = models.Student.objects.get(user__username=student_username)
        serializer.save(lesson=lesson, student=student)


class MarkRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Mark.objects
    serializer_class = serializers.MarkSerializer

    def perform_update(self, serializer):
        kwargs = {}
        if lesson_id := serializer.validated_data.pop('lesson_id'):
            lesson = models.Lesson.objects.get(pk=lesson_id)
            kwargs["lesson"] = lesson
        if student_username := serializer.validated_data.pop('student_username'):
            student = models.Student.objects.get(user__username=student_username)
            kwargs["student"] = student
        serializer.save(**kwargs)
