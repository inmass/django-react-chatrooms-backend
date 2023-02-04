from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
import re

def strongPasswordValidator(password):
    errors = []
    if not re.search(r'\d', password):
        error = 'Password must contain at least one number.'
        errors.append(error)
    
    if not re.search(r'[A-Z]', password):
        error = 'Password must contain at least one uppercase letter.'
        errors.append(error)
    
    if not re.search(r'[a-z]', password):
        error = 'Password must contain at least one lowercase letter.'
        errors.append(error)
    
    if len(password) < 8:
        error = 'Password must be at least 8 characters long.'
        errors.append(error)

    return errors

class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirmation')

        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        user.save()
        return user
