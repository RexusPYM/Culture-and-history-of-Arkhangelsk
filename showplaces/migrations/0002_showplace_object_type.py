# Generated by Django 4.1.5 on 2023-02-07 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showplaces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='showplace',
            name='object_type',
            field=models.CharField(default='showplace', max_length=10),
        ),
    ]
