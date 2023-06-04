# Generated by Django 2.0 on 2022-04-06 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0023_auto_20220402_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loanType', models.CharField(max_length=100, null=True)),
                ('fro', models.DateField(null=True)),
                ('to', models.DateField(null=True)),
                ('emi', models.CharField(max_length=30, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]