# Generated by Django 3.0.2 on 2020-01-18 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='state',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
