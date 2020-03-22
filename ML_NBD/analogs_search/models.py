from django.db import models

# Create your models here.
ANALOGS_OUT = 'media/sdf'


class AnalogsModel(models.Model):
    query_sdf = models.FileField(upload_to=ANALOGS_OUT)
    email = models.CharField(default='...@gmail.com', max_length=100)

    def __str__(self):
        return self.query_sdf
