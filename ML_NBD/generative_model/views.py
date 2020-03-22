from django.shortcuts import render, redirect
from . import forms as fo
from. import tasks as hp
from django.http import HttpResponse, FileResponse
import os
from . import  models as mo
from ML_NBD import views as vw



# Create your views here.


def success(request):
    return render(request, "generative_model/success.html")


def home(request):
    context = {
        'form': fo.GenerativeForm()
    }
    if request.method == "POST":
        form = fo.GenerativeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            complex = form.cleaned_data
            input_path = os.path.abspath(os.path.join(mo.GENERATIVE_OUT, str(complex["pdb"])))
            iterations = complex["iterations"]
            resname = complex["residue_name"]
            email = complex["email"]
            hp.launch_generative_workflow.delay(input_path, resname, iterations, email)
            return render(request, "generative_model/success.html", {"text":vw.SUCCESS.format(email)})
        else:
            raise(form.errors)
    else:
        return render(request, "generative_model/generative.html", context)

def RNN(request):
    return render(request, "generative_model/rnn.html")

def VAE(request):
    return render(request, "generative_model/vae.html")

