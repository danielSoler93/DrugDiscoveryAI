import os
import tempfile
import subprocess
import xtarfile as tarfile



class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


def launch_generative_model(input_path):
    command = "python -m growai.grow --pdb {} --resname TOL --only_grow --grow_iterations 2 ".format(input_path)
    tmp_dir = tempfile.mkdtemp()
    with cd(tmp_dir):
        subprocess.call(command.split())
    return tmp_dir


def make_zip(source_dir, output_filename="results.zip"):
    command = "zip -r {} {}".format(output_filename, source_dir)
    subprocess.call(command.split())
    return output_filename