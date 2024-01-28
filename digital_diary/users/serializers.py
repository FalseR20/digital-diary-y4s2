from rest_framework import serializers

from digital_diary.diary import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username', 'first_name', 'last_name', 'password')

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        return user
