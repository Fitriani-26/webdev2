# Generated by Django 4.2.1 on 2023-06-14 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pdaftar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('jenis_kelamin', models.CharField(max_length=20)),
                ('alamat', models.CharField(max_length=200)),
                ('no_telp', models.CharField(max_length=50)),
            ],
        ),
    ]