from rest_framework import generics

from . import serializers, models


class MarkAPIView(generics.ListAPIView):
    queryset = models.Mark.objects.all()
    serializer_class = serializers.MarkSerializer
