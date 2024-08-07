# Generated by Django 5.0.6 on 2024-06-25 02:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('favorite_id', models.AutoField(primary_key=True, serialize=False)),
                ('favorite_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.projects')),
                ('user_favorite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
