# Generated by Django 2.0 on 2022-04-19 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_esalary_sata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='esalary',
            old_name='sat',
            new_name='AllowanceType',
        ),
        migrations.RenameField(
            model_name='esalary',
            old_name='sata',
            new_name='aa',
        ),
    ]
