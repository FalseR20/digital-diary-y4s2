from rest_framework import generics

from digital_diary.diary import models, serializers


class TeacherListAPIView(generics.ListAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer


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
