from rest_framework import generics

from digital_diary.diary import models, serializers


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
