# Generated by Django 4.1.2 on 2024-07-11 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0009_bicicleta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='images/'),
        ),
    ]