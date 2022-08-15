from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from .models import Names_Gender
from .serializer import NamesSerializer


class EventSerializer(ModelSerializer):

    class Meta:
        model = Names_Gender
        exclude = ['user']




class NamesListView(ListCreateAPIView):

    queryset = Names_Gender.objects.all()
    serializer_class = NamesSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        es = EventSerializer(data=request.data)
        if es.is_valid():
            es.save(user=self.request.user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(data=es.errors, status=status.HTTP_400_BAD_REQUEST)



class NamesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Names_Gender.objects.all()
    serializer_class = NamesSerializer
    permission_classes = [IsAuthenticated ]