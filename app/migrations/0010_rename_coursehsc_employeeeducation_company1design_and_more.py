# Generated by Django 4.0.3 on 2022-03-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_percentagegra_employeeleaves_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeeducation',
            old_name='coursehsc',
            new_name='company1design',
        ),
        migrations.RenameField(
            model_name='employeeeducation',
            old_name='coursepg',
            new_name='company1duration',
        ),
        migrations.RenameField(
            model_name='employeeeducation',
            old_name='coursepggra',
            new_name='company1name',
        ),
        migrations.RenameField(
            model_name='employeeeducation',
            old_name='coursessc',
            new_name='company1salary',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='percentagegra',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='percentagehsc',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='percentagepg',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='percentagessc',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='schoolclggra',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='schoolclghsc',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='schoolclgpg',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='schoolclgssc',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='yearofpassinghsc',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='yearofpassingpg',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='yearofpassingra',
        ),
        migrations.RemoveField(
            model_name='employeeeducation',
            name='yearofpassingssc',
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='company2design',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='company2duration',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='company2name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='company2salary',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='company3design',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='company3duration',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='company3name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employeeeducation',
            name='company3salary',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
