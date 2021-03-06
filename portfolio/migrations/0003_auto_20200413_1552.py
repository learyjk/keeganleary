# Generated by Django 3.0.5 on 2020-04-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_link',
            field=models.URLField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='project',
            name='long_description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
