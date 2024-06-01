# Generated by Django 4.2.7 on 2024-05-30 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0008_blogpost_benefits_blogpost_how_to_use_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='tags',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to='home_page.tag'),
        ),
    ]