from django.shortcuts import render
from django.http import HttpResponse

SUCCESS = "Results have been sent to {}. \
    If something went wrong, please, let us know at \
    daniel.soler@nostrumbiodiscovery.com. We will \
    contact you as soon as possible"

def home(request):
    return render(request, "generative_model/home.html")
