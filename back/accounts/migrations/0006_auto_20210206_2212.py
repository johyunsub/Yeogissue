# Generated by Django 3.1.3 on 2021-02-06 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_myuser_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
