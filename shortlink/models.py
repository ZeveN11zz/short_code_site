from django.db import models
from django.utils.crypto import get_random_string


# Create your models here.
class RedirectLink(models.Model):
    short_code = models.SlugField(max_length=8, null=True, blank=True, verbose_name='Короткий код, добавляеый к ссылке')
    url = models.CharField(max_length=255, verbose_name='Полный url')
    stop_count = models.IntegerField(null=True, blank=True, verbose_name='Ограничение на кол-во переходов')
    stop_date = models.DateField(null=True, blank=True, verbose_name="Дата отключения")
    rdir_count = models.IntegerField(default=0, verbose_name='Кол-во переходов')
    
    def __str__(self):
        return self.url
    
    # Метод для генерации короткого кода, добавляемого к ссылке
    def generane_short_code(self):
        while True:
            self.short_code = get_random_string(8)
            dublicate_objects = type(self).objects.filter(short_code=self.short_code)
            if not len(dublicate_objects):
                break
        super(RedirectLink, self).save()