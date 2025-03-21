from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     return user   
    
    def create(self, validated_data):
        #create - save the password in plain text
        #create_user - save the hash password
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user