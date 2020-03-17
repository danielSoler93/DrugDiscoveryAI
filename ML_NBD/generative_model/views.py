from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
MODELS = [
    {"title": "rnn"},
    {"title": "vae" }
]

def home(request):
    context = {
        'models' : MODELS
    }
    return render(request, "generative_model/home.html", context)

def RNN(request):
    return render(request, "generative_model/rnn.html")

def VAE(request):
    return render(request, "generative_model/vae.html")