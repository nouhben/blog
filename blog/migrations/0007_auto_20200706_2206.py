# Generated by Django 3.0.7 on 2020-07-06 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_comment_has_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='post',
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
