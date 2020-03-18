from django.shortcuts import render
from django.http import HttpResponse
from . import forms as fo

# Create your views here.
def home(request):
    context = {
        'form' : fo.GenerativeForm()
    }
    if request.method == "POST":
        form = fo.GenerativeForm(request.POST)
        if form.is_valid():
            complex = form.cleaned_data["complex"]
            print(complex)
            #DO STUFF AND REDIRECT TO LANDING PAGE
        return render(request, "generative_model/generative.html", context)
    else:
        return render(request, "generative_model/generative.html", context)

def RNN(request):
    return render(request, "generative_model/rnn.html")

def VAE(request):
    return render(request, "generative_model/vae.html")

