from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True,)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts')

    group = models.ForeignKey(
        'Group',
        blank=True,
        null=True,
        on_delete=models.CASCADE)


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


'''
# Ещё вариант модели

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Event(models.Model):
    name = models.CharField(max_length=200)
#           # поле символов максимальная длина - 400
    start_at = models.DateTimeField(auto_now_add=True)
#           # автоматическое добавление даты публикации
    description = models.TextField()
#           # обычное текстовое поле, можно без указания длины строки
    contact = models.EmailField()
#           # можно не указывать ничего в этом проекте,
#           # но в целом - лучше указать
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="events")
#           # вторичный ключ, соединяется с первичным по связи 'contact'
    location = models.CharField(max_length=400)
#           # поле символов максимальная длина - 400
'''
