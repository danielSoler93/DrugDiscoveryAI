# Generated by Django 3.0 on 2020-03-22 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generative_model', '0003_auto_20200319_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='generativemodel',
            name='email',
            field=models.CharField(default='...@gmail.com', max_length=100),
        ),
    ]