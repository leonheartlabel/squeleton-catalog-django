# Generated by Django 4.2.9 on 2024-01-08 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_created_at_post_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default='NO CONTEXT'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(max_length=255),
        ),
    ]
