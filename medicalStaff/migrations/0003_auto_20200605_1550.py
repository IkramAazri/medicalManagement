# Generated by Django 3.0.5 on 2020-06-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalStaff', '0002_auto_20200605_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='profession',
            field=models.CharField(default='sans profession', max_length=50, null=True),
        ),
    ]