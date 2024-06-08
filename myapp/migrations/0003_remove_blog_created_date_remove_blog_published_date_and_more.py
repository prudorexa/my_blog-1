# Generated by Django 5.0.6 on 2024-06-07 07:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_subscriber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='published_date',
        ),
        migrations.AddField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(),
        ),
    ]
