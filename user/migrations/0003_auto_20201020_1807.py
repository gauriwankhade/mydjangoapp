# Generated by Django 3.0.1 on 2020-10-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201020_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='date_of_birth',
            field=models.DateField(auto_now_add=True),
        ),
    ]
