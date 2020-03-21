from django.shortcuts import render
from django.http import FileResponse
from . import forms as fo
from . import tasks as hp
from . import models as mo
import os

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
                        output_dir = hp.launch_analogs_finder(query_molecule, database)
                        zip_file = hp.make_zip(output_dir)
                        zip_file_obj = open(zip_file, 'rb')
                        os.remove(zip_file)
                        return FileResponse(zip_file_obj)
                else:
                        print(form.errors)
        return render(request, "analogs_search/home.html", context)
