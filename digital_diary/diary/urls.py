from django.urls import path

from . import views

urlpatterns = [
    path('marks/', views.MarkAPIView.as_view(), name='marks'),
]
