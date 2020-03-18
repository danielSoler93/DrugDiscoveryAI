from django.db import models

# Create your models here.
GENERATIVE_OUT = 'media/sdf'

class GenerativeModel(models.Model):
    sdf = models.FileField(upload_to=GENERATIVE_OUT)

    def __str__(self):
        return self.sdf