# Generated by Django 3.0.2 on 2020-01-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200116_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='iban',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
