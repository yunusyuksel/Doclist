# Generated by Django 3.0 on 2021-05-09 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0011_auto_20210509_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='telephone',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]