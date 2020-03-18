from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='generative-home'),
    path('RNN', views.RNN, name='generative-rnn'),
    path('VAE', views.VAE, name='generative-vae'),
    path('success', views.success, name='generative-success')
]