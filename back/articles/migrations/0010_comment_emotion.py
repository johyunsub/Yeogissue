# Generated by Django 3.1.3 on 2021-02-06 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20210206_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='emotion',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
