# Generated by Django 3.2.6 on 2021-08-22 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codewazlar', '0008_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=256)),
                ('phone_number', models.CharField(blank=True, max_length=16, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='ourdetail/')),
            ],
        ),
    ]
