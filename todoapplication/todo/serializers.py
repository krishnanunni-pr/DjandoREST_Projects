from rest_framework.serializers import ModelSerializer
from todo.models import Todo
from django.contrib.auth.models import User

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['task_name', 'user']



class UserCreationSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email','password']
