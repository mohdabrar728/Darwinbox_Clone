# Generated by Django 3.2.5 on 2021-08-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_alter_attendance1_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance1',
            name='total_work_duration',
            field=models.CharField(default=2, max_length=70),
            preserve_default=False,
        ),
    ]
