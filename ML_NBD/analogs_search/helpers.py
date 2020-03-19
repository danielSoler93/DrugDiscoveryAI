import os
import tempfile
import subprocess



class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


def launch_analogs_finder(query_molecule, database):
    command = "python -m analogs_finder.main {} {} --fp_type DL circular torsions MACCS --tresh 0.7 0.4 0.7 0.7".format(
        database, query_molecule)
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