from django.urls import path
from . import views

urlpatterns = [
    path('api/drawings', views.DrawingsList.as_view()),
    path('api/drawings/<int:pk>', views.PostRetrieveDeleteDrawing.as_view()),
    path('api/drawing/<title>', views.RetrieveDrawing.as_view()),
]