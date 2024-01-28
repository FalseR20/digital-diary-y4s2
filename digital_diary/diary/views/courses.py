from rest_framework import generics

from digital_diary.diary import models, serializers


class CourseListAPIView(generics.ListAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class CourseCreateAPIView(generics.CreateAPIView):
    queryset = models.Course.objects
    serializer_class = serializers.CourseSerializer


class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
