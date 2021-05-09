# Generated by Django 3.0 on 2021-05-09 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='staffs/')),
                ('default', models.BooleanField(default=False)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Staff')),
            ],
        ),
    ]