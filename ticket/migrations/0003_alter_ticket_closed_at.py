# Generated by Django 4.0.5 on 2022-06-11 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_alter_department_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='closed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
