from django.db import models
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    category = models.CharField('Категорія', max_length=250, help_text='Максимум 250 символів')
    slug = models.SlugField('Слаг', null=True, blank=True)

    class Meta:
        verbose_name = 'Категорія для публікації'
        verbose_name_plural = 'Категорії для публікацій'

    def _str__(self):
        return self.category


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=250, help_text='Максимум 250 символів')
    description = models.TextField(blank=True, null=True, verbose_name='Опис')
    pub_date = models.DateTimeField('Дата публікації', default=timezone.now)
    slug = models.SlugField('Слаг', unique_for_date='pub_date')
    main_page = models.BooleanField('Головна', default=False, help_text='Показувати на головній сторінці')
    category = models.ForeignKey(Category, related_name='articles', blank=True, null=True, verbose_name='Категорія',
                                 on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = u'Стаття'
        verbose_name_plural = u'Статті'

    def _str__(self):
        return self.title
