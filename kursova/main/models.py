from django.db import models

class Task(models.Model):
    equation = models.CharField('Рівняння', max_length=50)
    data = models.TextField('Дані')
    
    def __str__(self):
        return self.equation

    class Meta:
        verbose_name ='Рівняння'
        verbose_name_plural ='Рівняннь'