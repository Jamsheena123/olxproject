# Generated by Django 4.2.5 on 2023-09-26 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_vehicles_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicles',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
