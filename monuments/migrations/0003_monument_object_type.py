# Generated by Django 4.1.5 on 2023-02-07 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monuments', '0002_alter_monument_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='monument',
            name='object_type',
            field=models.CharField(default='monument', max_length=10),
        ),
    ]
