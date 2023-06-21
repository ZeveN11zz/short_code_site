import datetime
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import RedirectLink
from .forms import RdirLink


def main_page(request):
    # Отрисока главной страницы с формой для сокращения
    if request.method == "POST":
        # Если была отправленна форма, проверяем ее на валидность,
        # Генерируем короткий код для ссылки и сохраняем в бд
        form = RdirLink(request.POST)
        if form.is_valid():
            rdir_link = form.save(commit=False)
            rdir_link.generane_short_code()
            rdir_link.save()
            return redirect('result_page', pk=rdir_link.short_code)
    else:
        form = RdirLink()
        return render(request, 'shortlink/welcome.html', {"form": form})


def result_page(request, pk):
    result_link = RedirectLink.objects.get(short_code=pk)
    return render(request, 'shortlink/result.html', {"result_link": result_link})


def rdir_link(request, pk):
    # Редирект пользователя на сокращщенную ссылку
    
    # Ищем нужную нам ссылу по шорт коду.
    # Если не находим - перебрасываем на 404
    try:
        result_link = RedirectLink.objects.get(short_code=pk)
    except ObjectDoesNotExist:
        raise Http404
    
    # Добавляем счетчик посещений
    result_link.rdir_count += 1
    
    # Если было ограничение на кол-во посещений,
    # удаляем ссылку из бд и перекидываем на 404
    if result_link.stop_count:
        if result_link.rdir_count > result_link.stop_count:
            result_link.delete()
            raise Http404
        
    # Анологично если было ограничение по дате,
    # удаляем ссылку из бд и перекидываем на 404
    if result_link.stop_date:
        if datetime.date.today() > result_link.stop_date:
            result_link.delete()
            raise Http404
        
    # Сохраняем 
    result_link.save()
    return HttpResponseRedirect(result_link.url)


def not_found(request, exception):
    # Отрисовка страницы 404
    return render(request, 'shortlink/404.html', status=404)