# Generated by Django 3.0 on 2021-05-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0005_auto_20210509_0834'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicStaffProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Bilinmiyor')], max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='StaffProfile',
        ),
    ]