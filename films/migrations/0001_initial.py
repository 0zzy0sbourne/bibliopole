# Generated by Django 4.0.6 on 2022-07-16 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_title', models.CharField(max_length=200)),
                ('film_director', models.CharField(max_length=200)),
                ('film_rating', models.FloatField()),
            ],
        ),
    ]
