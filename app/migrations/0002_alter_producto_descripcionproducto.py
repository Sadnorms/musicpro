# Generated by Django 4.2 on 2023-05-29 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcionProducto',
            field=models.TextField(max_length=600),
        ),
    ]