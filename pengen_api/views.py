from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Drawing
from .serializers import DrawingSerializer


# Create your views here.
class DrawingsList(ListCreateAPIView):
    queryset = Drawing.objects.all()
    serializer_class = DrawingSerializer


class PostRetrieveDeleteDrawing(RetrieveUpdateDestroyAPIView):
    queryset = Drawing.objects.all()
    serializer_class = DrawingSerializer


