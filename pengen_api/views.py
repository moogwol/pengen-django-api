from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Drawing
from .serializers import DrawingSerializer


# Create your views here.
class DrawingsList(ListCreateAPIView):
    queryset = Drawing.objects.all()
    serializer_class = DrawingSerializer


class PostRetrieveDeleteDrawing(RetrieveUpdateDestroyAPIView):
    queryset = Drawing.objects.all()
    serializer_class = DrawingSerializer


class RetrieveDrawing(RetrieveAPIView):
    queryset = Drawing.objects.all()
    serializer_class = DrawingSerializer
    lookup_field = 'title'








