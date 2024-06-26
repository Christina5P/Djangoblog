# Generated by Django 4.2.13 on 2024-06-19 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL),
        ),
    ]