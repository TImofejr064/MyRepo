from django.shortcuts import render, get_object_or_404, redirect
from .models import Solution
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup


def main_page(request):
    source = requests.get('https://gdz.ru/class-7/algebra/makarychev-uglublennoe-izuchenie/', headers = {'User-Agent' : UserAgent().firefox}).text
    soup = BeautifulSoup(source, 'lxml')
    block = soup.find('section', class_="active")
    numbers = block.div
    for number in numbers.find_all('a'):
        try:
            n = number.text
            t = soup.h1.text
            source_i = requests.get(f'https://gdz.ru/class-7/algebra/makarychev-uglublennoe-izuchenie/{n}-nom/').text
            soup = BeautifulSoup(source_i, 'lxml')
            d = soup.find('div', class_='with-overtask')
            i_ur = d.img.attrs['src']
            source_i = requests.get(d.img.attrs['src'][2::]).text
            soup = BeautifulSoup(source_i, 'lxml')
            d = soup.find('body')
            i_ur = d.img.attrs['src']

            ar = Solution(book=t, number_of_task=n, image=i_ur[2::])
            ar.save()
        except :
            print('dont worry')
            continue

    # n = 77
    # source_i = requests.get(f'https://gdz.ru/class-7/algebra/makarychev-uglublennoe-izuchenie/{n}-nom/', headers = {'User-Agent' : UserAgent().firefox}).text
    # img_block = source_i.find('img', attrs = {'alt' : 'ГДЗ по алгебре 7 класс Ю.Н. Макарычев  Углубленный уровень номер - 74, решебник'}').src


    tasks_numbers = Solution.objects.all()
    context = {'tasks': tasks_numbers}
    return render(request, template_name='gdz/main.html', context=context)


def nom_detail(request, number_of_task):
    post = get_object_or_404(Solution, number_of_task=number_of_task)
    return render(request, template_name='gdz/detail.html', context={'post': post})


def redirect_page(request):
    return redirect('main-page')
