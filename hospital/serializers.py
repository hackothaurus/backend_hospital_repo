from .models import Doctor, Patient
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class DoctorSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self):
        print(self.validated_data['email'])
        # create a new user as well as a Registered user
        new_user = User.objects.create(
            email=self.validated_data['username'],
            username=self.validated_data['email'],
        )
        new_user.set_password(self.validated_data['password'])
        new_user.save()
        d =Doctor.objects.create(user=new_user)
        return d

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('name', 'appointment_date', 'diagnosis', 'doc', 'severity')