# Generated by Django 3.2.9 on 2021-11-26 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quadratic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quadratics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.IntegerField(verbose_name='Введіть коефіцієнт а')),
                ('b', models.IntegerField(verbose_name='Введіть коефіцієнт b')),
                ('c', models.IntegerField(verbose_name='Введіть коефіцієнт c')),
            ],
        ),
        migrations.DeleteModel(
            name='QuadraticApp',
        ),
    ]
