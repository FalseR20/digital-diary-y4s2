from rest_framework import generics

from digital_diary.diary import models, serializers


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
