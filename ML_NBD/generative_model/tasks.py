import os
import tempfile
import subprocess
from celery import shared_task
from django.http import HttpResponse, FileResponse
from . import models as mo
import os
from . import tasks as hp
from django.core.mail import send_mail
from django.core.mail import EmailMessage





class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)



def launch_generative_model(input_path, resname, iterations):
    command = "python -m growai.grow --pdb {} --resname {} --only_grow --grow_iterations {} ".format(
        input_path, resname, iterations)
    tmp_dir = tempfile.mkdtemp()
    with cd(tmp_dir):
        subprocess.call(command.split())
    return tmp_dir


def make_zip(source_dir, output_filename="results.zip"):
    output_filename = "results_{}.zip".format(
    os.path.basename(source_dir))
    command = "zip -r {} {}".format(output_filename, source_dir)
    subprocess.call(command.split())
    return output_filename

def download_zip(zip_file):
    zip_file_obj = open(zip_file, 'rb')
    os.remove(zip_file)
    return FileResponse(zip_file_obj)

@shared_task
def launch_generative_workflow(input_path, resname, iterations):
    output_dir = hp.launch_generative_model(input_path, resname, iterations)
    zip_file = hp.make_zip(output_dir)
    email = EmailMessage("NBDD-generative results",
                         "Here you have your results from NBD's generative model",
                         "dany.bcn.93@gmail.com",
                         ["daniel.soler@nostrumbiodiscovery.com"])
    email.attach_file(zip_file)
    email.send()
    return 'done'