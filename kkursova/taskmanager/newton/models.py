from django.db import models

class Newtons(models.Model):    
    f = models.CharField('Введіть функцію', max_length=35)
    x0 = models.FloatField('x0')
    max_iter = models.IntegerField('N')
    eps = models.FloatField('Введіть точність')

    def __str__(self):
        return f"{self.f}, {self.x0}, {self.max_iter}, {self.eps}"
