from django.urls import path
from .views import produto


urlpatterns = [
    path('produto', produto, name='produto')
]
