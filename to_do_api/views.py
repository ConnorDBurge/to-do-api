
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated 

from .serializers import UserProfileSerializer, UserToDoItemSerializer
from .models import UserProfile, ToDoItem
from .permissions import UpdateOwnProfile, UpdateOwnToDoItem


class UserProfileViewSet(viewsets.ModelViewSet):
    # api/profile/ (GET, POST)
    # api/profile/:id (GET, POST, PUT, PATCH, DELETE)
    """Handle creating and updating profiles"""
    serializer_class = UserProfileSerializer # How are we serializing the profile?
    queryset = UserProfile.objects.all() # Whats the dataset?
    authentication_classes = (TokenAuthentication,) # tuple
    permission_classes = (UpdateOwnProfile,) # tuple
    # api/profile/?search=<TERM>
    filter_backends = (filters.SearchFilter,) # tuple
    search_fields = ('first_name', 'last_name',) # tuple
    
    
class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    

class UserToDoViewSet(viewsets.ModelViewSet):
    """Handle creating and updating user profile feed items"""
    serializer_class = UserToDoItemSerializer
    authentication_classes = (TokenAuthentication,) # tuple
    queryset = ToDoItem.objects.all()
    permission_classes = (UpdateOwnToDoItem, IsAuthenticated,) # tuple
    # api/to-do/?search=<TERM>
    filter_backends = (filters.SearchFilter,) # tuple
    search_fields = ('task',) # tuple
    
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)