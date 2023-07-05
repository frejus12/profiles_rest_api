from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from profiles_api import models
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfilesSerializers
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfiles,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email',)
