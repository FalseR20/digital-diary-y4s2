from rest_framework import generics

from digital_diary.diary import models, serializers


class StudentListAPIView(generics.ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


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
