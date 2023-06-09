# Generated by Django 4.0.3 on 2022-03-27 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_rename_leavetype_employeeleaves_position_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeleaves',
            old_name='date',
            new_name='fro',
        ),
        migrations.RenameField(
            model_name='employeeleaves',
            old_name='Position',
            new_name='leaveType',
        ),
        migrations.RemoveField(
            model_name='employeeleaves',
            name='age',
        ),
        migrations.RemoveField(
            model_name='employeeleaves',
            name='city',
        ),
        migrations.RemoveField(
            model_name='employeeleaves',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employeeleaves',
            name='esalary',
        ),
        migrations.RemoveField(
            model_name='employeeleaves',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='employeeleaves',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='employeeleaves',
            name='no',
        ),
        migrations.RemoveField(
            model_name='employeeleaves',
            name='osalary',
        ),
        migrations.AddField(
            model_name='employeeleaves',
            name='description',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='employeeleaves',
            name='to',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employeeleaves',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='EmployeeJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Position', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('no', models.CharField(max_length=100, null=True)),
                ('age', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('esalary', models.CharField(max_length=100, null=True)),
                ('osalary', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
