# Generated by Django 4.2.7 on 2023-11-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criminal_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criminal_id', models.CharField(max_length=10000)),
                ('criminal_name', models.CharField(max_length=200)),
                ('crime_type', models.TextField()),
                ('criminal_image', models.ImageField(upload_to='media/criminal')),
            ],
        ),
    ]
