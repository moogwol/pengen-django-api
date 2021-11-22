from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView
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


# class RetrieveDrawing(RetrieveAPIView):
#     queryset = Drawing.objects.all()
#     serializer_class = DrawingSerializer
#     lookup_field = 'title'

class RetrieveADrawing(ListAPIView):
    serializer_class = DrawingSerializer

    def get_queryset(self):
        queryset = Drawing.objects.all()

        title = self.request.query_params.get('title')
        queryset = queryset.filter(title=title)

        return queryset





