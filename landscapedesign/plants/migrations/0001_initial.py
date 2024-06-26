# Generated by Django 5.0.4 on 2024-04-08 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название растения')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет растения')),
                ('height', models.FloatField(verbose_name='Высота растения')),
                ('description', models.TextField(verbose_name='Описание растения')),
                ('date', models.DateTimeField(verbose_name='Дата добавления')),
            ],
        ),
    ]
