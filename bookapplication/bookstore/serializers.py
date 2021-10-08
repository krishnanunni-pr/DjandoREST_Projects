from rest_framework.serializers import ModelSerializer
from bookstore.models import Book
from django.contrib.auth.models import User
from rest_framework import serializers

class UserCreationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']

        def create(self, validated_data):
            return User.objects.create_user(username=validated_data['username'],
                                            password=validated_data['password'], email=validated_data['email'])


class BookSerializer(ModelSerializer):
    user = UserCreationSerializer
    class Meta:
        model = Book
        fields = ['book_name','author','price','copies','user']



class LoginSerializer(serializers.Serializer):

    username=serializers.CharField()
    password=serializers.CharField()