from django.shortcuts import render, get_object_or_404
from .models import Solution
import requests
from bs4 import BeautifulSoup

def main_page(request):
    # source = requests.get('https://gdz.ru/class-7/algebra/makarychev-uglublennoe-izuchenie/').text
    # soup = BeautifulSoup(source, 'lxml')
    # block = soup.find('section', class_="active")
    # numbers = block.div
    # for number in numbers.find_all('a'):
    #     n = number.text
    #     t = soup.h1.text
    #     ar = Solution(book=t, number_of_task=n)
    #     ar.save()

    tasks_numbers = Solution.objects.all()
    context = {'tasks' : tasks_numbers}
    return render(request, template_name='gdz/main.html', context=context)

def nom_detail(request, number_of_task):
    post = get_object_or_404(Solution, number_of_task=number_of_task)
    return render(request, template_name='gdz/detail.html', context={'post' : post})