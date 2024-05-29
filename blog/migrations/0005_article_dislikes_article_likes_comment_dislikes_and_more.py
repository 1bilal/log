# Generated by Django 5.0.6 on 2024-05-29 20:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_article_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='disliked_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='disliked_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]