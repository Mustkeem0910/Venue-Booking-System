# Generated by Django 4.1.3 on 2022-11-19 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookable1', '0005_booked_community_halls_type_booked_gardens_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booked_community_halls',
            name='dateend',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='booked_community_halls',
            name='datestart',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='booked_gardens',
            name='dateend',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='booked_gardens',
            name='datestart',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='booked_halls',
            name='dateend',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='booked_halls',
            name='datestart',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='booked_pools',
            name='dateend',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='booked_pools',
            name='datestart',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='requested_community_hall',
            name='dateend',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='requested_community_hall',
            name='datestart',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='requested_garden',
            name='dateend',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='requested_garden',
            name='datestart',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='requested_hall',
            name='dateend',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='requested_hall',
            name='datestart',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='requested_pool',
            name='dateend',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='requested_pool',
            name='datestart',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='community_hall',
            name='img',
            field=models.ImageField(upload_to='Photos/'),
        ),
        migrations.AlterField(
            model_name='garden',
            name='img',
            field=models.ImageField(upload_to='Photos/'),
        ),
        migrations.AlterField(
            model_name='hall',
            name='img',
            field=models.ImageField(upload_to='Photos/'),
        ),
        migrations.AlterField(
            model_name='pool',
            name='img',
            field=models.ImageField(upload_to='Photos/'),
        ),
    ]
