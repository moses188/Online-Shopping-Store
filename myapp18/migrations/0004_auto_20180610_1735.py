# Generated by Django 2.0.5 on 2018-06-10 21:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp18', '0003_auto_20180609_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]