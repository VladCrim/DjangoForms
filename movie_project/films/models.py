from django.db import models

class Film(models.Model):
    title = models.CharField('Название фильма', max_length=200)
    description = models.TextField('Описание фильма')
    review = models.TextField('Отзыв о фильме')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title
