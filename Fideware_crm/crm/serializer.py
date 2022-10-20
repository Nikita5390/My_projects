from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name', 'last_name', 'job_title',
            'company', 'email', 'linkedin',
            'add_contact', 'group', 'last_contact', 'next_contact',
            'status', 'step', 'comment', 'history',
        ]

    # def create(self, validated_data):
    #     return UserHistory.objects.create(**validated_data)
