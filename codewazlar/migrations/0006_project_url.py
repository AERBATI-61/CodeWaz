# Generated by Django 3.2.6 on 2021-08-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codewazlar', '0005_risejob'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
