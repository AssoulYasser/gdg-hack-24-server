from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

@api_view(['POST'])
def sign_up(request):
    data = request.data
    serializer = SignUpSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=200, data=serializer.validated_data)
    print(serializer.errors)
    return Response(status=400)

@api_view(['GET'])
def sign_in(request):
    data = request.data
    serializer = SignInSerializer(data=data)
    if serializer.is_valid():
        try:
            profile = Profile.objects.get(email=serializer.validated_data['email'])
        except:
            return Response(status=4004)
        if check_password(serializer.validated_data['password'], profile.password):
            serializer = SignUpSerializer(instance=profile)
            return Response(status=200, data=serializer.data)
    print(serializer.errors)
    return Response(status=400)
