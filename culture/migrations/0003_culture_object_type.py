# Generated by Django 4.1.5 on 2023-02-07 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culture', '0002_rename_custom_culture'),
    ]

    operations = [
        migrations.AddField(
            model_name='culture',
            name='object_type',
            field=models.CharField(default='culture', max_length=10),
        ),
    ]
