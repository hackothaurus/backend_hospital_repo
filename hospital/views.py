from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from django.views.generic import ListView
from .models import Doctor, Patient, User
from django.http import Http404
from rest_framework.decorators import api_view
from .serializers  import DoctorSerializer, PatientSerializer
from django.core import serializers
from django.contrib.auth import authenticate
#from django.contrib.auth.models import User

@api_view(["GET","POST"])
def doc(request):
    if request.method == 'POST':
        data = request.data['data']
        print(data)
        user1 = User.objects.create(username=data['username'], email=data['email'], password=data['password'])
        Doctor.objects.create(user=user1)
        return Response(status=status.HTTP_201_CREATED)

@api_view(["GET"])
def authenticate(request):
    username = request.query_params['username']
    password = request.query_params['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        Response(status=status.HTTP_200_OK)
    else:
        Response(status=status.HTTP_401_UNAUTHORIZED)
        
@api_view(["GET"])
def allPatients(request):
    email = request.query_params['docemail']
    severity = request.query_params['severity']
    try:
        user = User.objects.get(email=email)
        docuser = Doctor.objects.get(user=user)
        patients = Patient.objects.filter(doc=docuser, severity=severity)
        serializer = PatientSerializer(patients, many=True)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)

@api_view(["DELETE"])
def deletePatient(request):
    data = request.data
    Patient.objects.filter(name = data['name'], doc=data['doc']).delete()
    return Response(status=status.HTTP_200_OK)

@api_view(["PUT"])
def editPatient(request):
    data = request.data
    Patient.objects.filter(name = data['name'], doc=data['doc']).delete()
    Patient.objects.create(name=data['name'],appointment_date=data['appointment_date'],doc=data['doc'],diagnosis=data['diagnosis'],severity=data['severity'])
    return Response(status=status.HTTP_200_OK)

@api_view(["POST"])
def addPatient(request):
    data = request.data['data']
    docuser = User.objects.get(email=data['doctor_email'])
    doct = Doctor.objects.get(user=docuser)
    Patient.objects.create(name=data['name'], appointment_date=data['appointment'], diagnosis=data['diagnosis'], doc=doct, severity=data['severity'])
    return Response(status=status.HTTP_201_CREATED)
