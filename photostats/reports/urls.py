from django.urls import path

from . import views

app_name='reports'
urlpatterns = [
    path('', views.index, name='index'),
    path('timelines', views.timelines, name='timelines'),
    path('compare', views.compare, name='compare'),
]