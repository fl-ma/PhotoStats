from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListAllView.as_view())
]