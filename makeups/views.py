
from django.db import models
from django.shortcuts import render
from rest_framework import generics

from .models import product
from .serializer import makeupsSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class makeupsListView(generics.ListCreateAPIView):    
    serializer_class = makeupsSerializer
    queryset = product.objects.all()

class makeupsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = makeupsSerializer
    queryset = product.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)