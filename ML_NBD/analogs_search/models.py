from django.db import models

# Create your models here.
ANALOGS_OUT = 'media/sdf'


class AnalogsModel(models.Model):
    query_sdf = models.FileField(upload_to=ANALOGS_OUT)

    def __str__(self):
        return self.query_sdf
