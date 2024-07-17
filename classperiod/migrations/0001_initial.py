# Generated by Django 5.0.6 on 2024-07-17 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassPeriod',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=30)),
                ('class_start_time', models.TimeField()),
                ('class_end_date', models.TimeField()),
                ('class_dayofweek', models.CharField(max_length=30)),
            ],
        ),
    ]