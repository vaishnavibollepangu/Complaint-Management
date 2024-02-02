# Generated by Django 4.0.5 on 2022-07-22 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_managementapp', '0004_send_query'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query_Replay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('solvers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint_managementapp.solvers')),
            ],
            options={
                'db_table': 'Query_Replay',
            },
        ),
    ]