# Generated by Django 4.2.5 on 2023-09-25 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('tank', 'Танки'), ('heal', 'Хилы'), ('dd', 'ДД'), ('merch', 'Торговцы'), ('gm', 'Гилдмастеры'), ('qg', 'Квестгиверы'), ('smith', 'Кузнецы'), ('tan', 'Кожевники'), ('pm', 'Зельевары'), ('sm', 'Мастера заклинаний')], default='tank', max_length=5)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('_has_accepted_reply', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', 'title'],
            },
        ),
        migrations.CreateModel(
            name='ReplyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_accepted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='advertisements.advertmodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', 'user'],
            },
        ),
    ]
