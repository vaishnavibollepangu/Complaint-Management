# Generated by Django 4.0.5 on 2022-07-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_managementapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcatagory',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
