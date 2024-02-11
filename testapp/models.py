from django.db import models
# from django.contrib.auth.models import User


# Create your models here.


# Таблица страниц
class Pages(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


# Таблица новостей
class News(models.Model):
    title = models.CharField(max_length=64)
    head = models.CharField(max_length=128)
    image = models.ImageField(upload_to='media')
    disc = models.TextField(blank=True)
    pages_news = models.ForeignKey(Pages, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comments(models.Model):
    user_name = models.CharField(max_length=256)
    user_news = models.ForeignKey(News, on_delete=models.CASCADE)
    user_comment = models.TextField(blank=True)
    user_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
