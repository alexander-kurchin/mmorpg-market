from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class AdvertModel(models.Model):
    """
    Объявления состоят из заголовка и текста,
    внутри которого могут быть картинки, встроенные видео и другой контент.

    Кроме того, пользователь обязательно должен определить
    объявление в одну из следующих категорий:
                                    Танки, Хилы, ДД, Торговцы,
                                        Гилдмастеры, Квестгиверы,
                                            Кузнецы, Кожевники, Зельевары,
                                                Мастера заклинаний.
    """

    CATEGORIES = [('tank', 'Танки'),
                  ('heal', 'Хилы'),
                  ('dd', 'ДД'),
                  ('merch', 'Торговцы'),
                  ('gm', 'Гилдмастеры'),
                  ('qg', 'Квестгиверы'),
                  ('smith', 'Кузнецы'),
                  ('tan', 'Кожевники'),
                  ('pm', 'Зельевары'),
                  ('sm', 'Мастера заклинаний'),
                  ]

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORIES,
                                max_length=5,
                                default='tank')
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    _has_accepted_reply = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def has_accepted_reply(self):
        return self._has_accepted_reply

    @has_accepted_reply.setter
    def has_accepted_reply(self, value):
        self._has_accepted_reply = bool(value)
        self.save()

    class Meta:
        ordering = ['-created_at', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('advert_detail', args=[str(self.pk)])


class ReplyModel(models.Model):
    """
    Пользователи могут отправлять отклики на объявления
    других пользователей, состоящие из простого текста.
    """

    advert = models.ForeignKey(AdvertModel,
                               on_delete=models.CASCADE,
                               related_name='replies')
    user = models.ForeignKey(User,
                                on_delete=models.CASCADE)
    text = models.TextField()
    _is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_accepted(self):
        return self._is_accepted

    @is_accepted.setter
    def is_accepted(self, value):
        self._is_accepted = bool(value)
        self.save()

    class Meta:
        ordering = ['-created_at', 'user']
