# Generated by Django 4.0.5 on 2022-06-10 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin', to=settings.AUTH_USER_MODEL),
        ),
    ]
