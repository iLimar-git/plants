from django.db import models

class Plant(models.Model):
    name = models.CharField('Название растения', max_length=100)
    color = models.CharField('Цвет растения', max_length=50)
    height = models.FloatField('Высота растения (в см)')
    description = models.TextField('Описание растения')
    date = models.DateTimeField('Дата добавления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'

class Image(models.Model):
    title = models.CharField('Название', max_length=200)
    image = models.ImageField('Фото',upload_to='images')

    def __str__(self):
        return self.title