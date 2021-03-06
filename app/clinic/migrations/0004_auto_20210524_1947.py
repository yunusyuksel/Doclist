# Generated by Django 3.0 on 2021-05-24 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_title'),
        ('clinic', '0003_staff_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.Job'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.Title'),
        ),
    ]
