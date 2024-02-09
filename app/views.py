from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from django.http import QueryDict

@api_view(['POST'])
def sign_up(request):
    data = request.data
    serializer = SignUpSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=200, data=serializer.validated_data)
    print(serializer.errors)
    return Response(status=400)

@api_view(['POST'])
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

@api_view(['POST'])
def add_occupation(request):
    data = request.data
    serializer = OccupationSerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(status=200)
    return Response(status=400)

@api_view(['POST'])
def start_event(request):
    data = request.data
    serializer = EventSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=200)
    print(serializer.errors)
    return Response(status=400)

def set_users_as_occupied(dataset):
    users = []
    for data in dataset:
        users.append(data['profile'].email)
    
    Profile.objects.filter(email__in=users).update(is_occupied=True)

def is_user_occupied(dataset):
    for data in dataset:
        if data['profile'].is_occupied:
            return True
    set_users_as_occupied(dataset)
    return False

@api_view(['POST'])
def affect_mentors(request):
    data = request.data
    serializer = MentorSerializer(data=data, many=True)
    if serializer.is_valid():
        if is_user_occupied(serializer.validated_data):
            return Response(status=409)
        serializer.save()
        return Response(status=200)
    return Response(status=400)

@api_view(['POST'])
def affect_judge(request):
    data = request.data
    serializer = JudgeSerializer(data=data, many=True)
    if serializer.is_valid():
        if is_user_occupied(serializer.validated_data):
            return Response(status=409)
        serializer.save()
        return Response(status=200)
    return Response(status=400)