# Generated by Django 5.0.6 on 2024-06-27 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_projects_project_github_link_projects_project_tools_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorites',
            old_name='user_favorite',
            new_name='user',
        ),
    ]