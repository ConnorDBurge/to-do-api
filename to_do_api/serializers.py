from rest_framework import serializers
from .models import UserProfile, ToDoItem

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes the user profile"""
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True, # users wont be able to GET the password
                'style': { # makes the ••• show up when typing the password
                    'input_type': 'password',
                }
            }
        }
    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            password = validated_data['password']
        )
        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
    
        return super().update(instance, validated_data)