from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from user.models import User
from user.serializer import UserSerializer,UserRegistrationSerializer
from CustomUserModel.custom_permission import IsCreationOrIsAuthenticated

class UserView(ModelViewSet):
    queryset = User.objects.all()
   # serializer_class = UserSerializer
    permission_classes = [IsCreationOrIsAuthenticated]

    def get_serializer_class(self):
        serializer = None
        if self.action == 'create':
            serializer = UserRegistrationSerializer
        else:
            serializer = UserSerializer
        return serializer



class SpecificUserlView(APIView):
    #permission_classes = [IsAuthenticated, ]

    def get(self, request, id ,format=None):
        query_set = User.objects.get(id=id) #select * from details where id = id
        serializer = UserSerializer(query_set)
        return Response({'user': serializer.data})

