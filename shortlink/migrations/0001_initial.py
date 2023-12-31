# Generated by Django 4.2.2 on 2023-06-20 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RedirectLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_code', models.SlugField(max_length=8, verbose_name='Короткий код, добавляеый к ссылке')),
                ('url', models.CharField(max_length=255, verbose_name='Полный url')),
                ('stop_count', models.IntegerField(blank=True, null=True, verbose_name='Ограничение на кол-во переходов')),
                ('stop_date', models.DateField(blank=True, null=True, verbose_name='Дата отключения')),
            ],
        ),
    ]
