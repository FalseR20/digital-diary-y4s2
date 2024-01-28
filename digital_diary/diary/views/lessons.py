from rest_framework import generics

from digital_diary.diary import models, serializers


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
