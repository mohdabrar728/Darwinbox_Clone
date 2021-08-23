# Generated by Django 3.2.5 on 2021-08-23 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance1',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('clock_in', models.TimeField(null=True)),
                ('clock_out', models.TimeField(null=True)),
                ('total_work_duration', models.TimeField(null=True)),
                ('status', models.SlugField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]