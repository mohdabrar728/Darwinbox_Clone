# Generated by Django 3.2.5 on 2021-08-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('clock_in', models.TimeField(null=True)),
                ('clock_out', models.TimeField(null=True)),
                ('total_work_duration', models.TimeField(null=True)),
                ('status', models.SlugField()),
            ],
        ),
    ]