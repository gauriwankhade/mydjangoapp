# Generated by Django 3.0.1 on 2020-10-20 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201020_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
