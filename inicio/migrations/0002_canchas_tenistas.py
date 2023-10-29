# Generated by Django 4.2.6 on 2023-10-29 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canchas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('pais', models.CharField(max_length=30)),
                ('capacidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tenistas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('nacimiento', models.IntegerField()),
            ],
        ),
    ]
