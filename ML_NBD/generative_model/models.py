from django.db import models

# Create your models here.
GENERATIVE_OUT = 'media/sdf'


class GenerativeModel(models.Model):
    pdb = models.FileField(upload_to=GENERATIVE_OUT)
    residue_name = models.CharField(default='LIG', max_length=3)
    iterations = models.IntegerField(default=3)
    email = models.CharField(default='...@gmail.com', max_length=100)


    def __str__(self):
        return self.pdb