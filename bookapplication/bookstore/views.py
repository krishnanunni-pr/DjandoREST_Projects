from django.shortcuts import render
from rest_framework.views import APIView
from bookstore.models import Book
from bookstore.serializers import UserCreationSerializer,BookSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins,generics
from django.contrib.auth.models import User
from


# Create your views here.
