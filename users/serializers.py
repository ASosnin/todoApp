from rest_framework.serializers import ModelSerializer

from users.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']
