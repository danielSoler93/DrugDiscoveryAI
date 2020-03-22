import os
import tempfile
import subprocess
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from celery import shared_task




class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


@shared_task
def launch_analogsearch_workflow(query_molecule, database, email):
    command = "python -m analogs_finder.main {} {} --fp_type DL circular torsions MACCS --tresh 0.7 0.4 0.7 0.7".format(
        database, query_molecule)
    tmp_dir = tempfile.mkdtemp()
    with cd(tmp_dir):
        subprocess.call(command.split())
    output_filename = "results_{}.zip".format(
    os.path.basename(tmp_dir))
    command = "zip -r {} {}".format(output_filename, tmp_dir)
    subprocess.call(command.split())
    email = EmailMessage("NBDD-analogs results",
                         "Here you have your results from NBD's analog search",
                         "dany.bcn.93@gmail.com",
                         [email])
    email.attach_file(output_filename)
    email.send()
    return 'done'



