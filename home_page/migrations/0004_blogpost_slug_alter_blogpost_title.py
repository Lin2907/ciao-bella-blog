# Generated by Django 4.2.7 on 2024-05-13 12:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0003_remove_blogpost_excerpt_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]