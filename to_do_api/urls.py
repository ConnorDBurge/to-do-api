from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# API View Set uses the DefaultRouter
router = DefaultRouter()
# /api/profile/ (GET, POST)
# /api/profile/:id (GET, POST, PUT, PATCH, DELETE)
router.register('profile', views.UserProfileViewSet) # queryset provided in view set
router.register('to-do', views.UserToDoViewSet) # queryset provided in view set

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('', include(router.urls)), # see all routes in API
]