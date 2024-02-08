from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_user, name='login'),
    path('plataforma/', views.plataforma, name='plataforma')
] 