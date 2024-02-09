from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from django.http import QueryDict

def set_users_as_occupied(dataset):
    users = []
    for data in dataset:
        users.append(data['profile'].email)
    
    Profile.objects.filter(email__in=users).update(is_occupied=True)

def is_user_occupied(dataset):
    for data in dataset:
        print(data['profile'])
        if data['profile'].is_occupied:
            return True
    set_users_as_occupied(dataset)
    return False

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

@api_view(['POST'])
def set_agenda_activities(request):
    data = request.data
    serializer = AgendaSerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(status=200)
    print(serializer.errors)
    return Response(status=400)

@api_view(['POST'])
def team_registration(request):
    data = request.data
    serializer = TeamRegistrationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=200, data=serializer.validated_data)
    return Response(status=400)

@api_view(['POST'])
def participant_registration(request):
    data = request.data
    serializer = ParticipantRegisterationSerializer(data=data)
    if serializer.is_valid():
        if serializer.validated_data['profile'].is_occupied:
            return Response(status=409)
        serializer.save()
        return Response(status=200)
    return Response(status=400)

@api_view(['POST'])
def accept_team(request):
    data = request.data
    
    if 'ids' not in data:
        return Response(status=400)
    
    teams = data['ids']

    teams = TeamRegistration.objects.filter(id__in=teams)
    
    for team in teams:
        team_participants = ParticipantRegistration.objects.filter(team=team)

        team_instance = Team()
        team_instance.event = team.event
        team_instance.name = team.name

        team_instance.save()

        for participant in team_participants:
            participant_instance = Participant()
            participant_instance.profile = participant.profile
            participant_instance.team = team_instance

            participant_instance.save()

    return Response(status=200)

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