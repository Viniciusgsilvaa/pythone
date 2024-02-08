from django.urls import path
from .views import indexprod

urlpatterns =[
    path('prod', indexprod, name='indexprod')
]