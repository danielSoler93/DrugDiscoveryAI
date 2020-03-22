from django.shortcuts import render
from django.http import FileResponse
from . import forms as fo
from . import tasks as hp
from . import models as mo
import os
from ML_NBD import views as vw


# Create your views here.


def home(request):
        if request.method == "POST":
                form = fo.AnalogsForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save()
                        complex = form.cleaned_data
                        query_molecule = os.path.abspath(os.path.join(mo.ANALOGS_OUT, str(complex["query_sdf"])))
                        email = complex["email"]
                        database = "/Users/nostrum/repos/growai/growai/examples/analogs_finder/examples/database.sdf"
                        hp.launch_analogsearch_workflow.delay(query_molecule, database, email)
                        return render(request, "analogs_search/success.html", {"text":vw.SUCCESS.format(email)})
                else:
                        print(form.errors)
        context = {
                'form': fo.AnalogsForm()
        }
        return render(request, "analogs_search/home.html", context)
