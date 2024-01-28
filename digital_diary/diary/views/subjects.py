from rest_framework import generics

from digital_diary.diary import models, serializers


class SubjectListAPIView(generics.ListAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer


class SubjectCreateAPIView(generics.CreateAPIView):
    queryset = models.Subject.objects
    serializer_class = serializers.SubjectSerializer


class SubjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
