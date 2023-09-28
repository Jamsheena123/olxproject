# Generated by Django 4.2.5 on 2023-09-25 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('owner', models.CharField(max_length=200)),
                ('fuel_type', models.CharField(max_length=200)),
                ('kilometre', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]