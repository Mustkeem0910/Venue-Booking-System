# Generated by Django 4.1.3 on 2022-11-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookable1', '0008_remove_booked_community_halls_dateb_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='queries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=500)),
                ('query', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='replies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=500)),
                ('query', models.CharField(max_length=1500)),
                ('reply', models.CharField(max_length=1500)),
            ],
        ),
    ]
