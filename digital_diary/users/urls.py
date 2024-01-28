from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserListAPIView.as_view(), name='user-list'),
    path('new/', views.UserCreateAPIView.as_view(), name='user-list'),
    path('<str:username>/', views.UserRetrieveUpdateDestroyAPIView.as_view(),
         name='user-get'),
]
