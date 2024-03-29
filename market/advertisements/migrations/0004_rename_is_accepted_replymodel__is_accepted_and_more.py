# Generated by Django 4.2.5 on 2023-09-26 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisements', '0003_alter_advertmodel_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='replymodel',
            old_name='is_accepted',
            new_name='_is_accepted',
        ),
        migrations.AlterField(
            model_name='replymodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
