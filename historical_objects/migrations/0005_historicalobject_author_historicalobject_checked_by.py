# Generated by Django 4.1.5 on 2024-01-11 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('historical_objects', '0004_temporaryhistoricalobject_proposedhistoricalobject'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('object_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                                  to='historical_objects.objecttypes')),
                ('checked_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                                 related_name='checked_by', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                             related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
