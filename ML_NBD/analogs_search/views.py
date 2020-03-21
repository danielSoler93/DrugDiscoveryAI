from django.shortcuts import render
from django.http import FileResponse
from . import forms as fo
from . import tasks as hp
from . import models as mo
import os
from django.http import HttpResponse, FileResponse


# Create your views here.


def home(request):
        context = {
                'form': fo.AnalogsForm()
        }
        if request.method == "POST":
                form = fo.AnalogsForm(request.POST, request.FILES)
                if form.is_valid():
                        form.save()
                        complex = form.cleaned_data
                        query_molecule = os.path.abspath(os.path.join(mo.ANALOGS_OUT, str(complex["query_sdf"])))
                        database = "/Users/nostrum/repos/growai/growai/examples/analogs_finder/examples/database.sdf"
                        hp.launch_analogsearch_workflow.delay(query_molecule, database)
                        return HttpResponse('work kicked off!')
                else:
                        print(form.errors)
        return render(request, "analogs_search/home.html", context)
