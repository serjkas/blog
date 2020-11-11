from django.db import models


class Article(models.Model):
    title = models.CharField('Название', max_length=100, default='')
    anons = models.CharField('Анонс', max_length=250, default='')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата и время публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


    def get_absolute_url(self):
        return f'/news/{self.id}'