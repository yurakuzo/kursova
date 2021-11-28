from django.db import models


class Quadratics(models.Model):    
    a = models.IntegerField('Введіть коефіцієнт а')
    b = models.IntegerField('Введіть коефіцієнт b')
    c = models.IntegerField('Введіть коефіцієнт c')
    # roots = models.TextField(default='')

    def __str__(self):
        return f"{self.a}, {self.b}, {self.c}"
