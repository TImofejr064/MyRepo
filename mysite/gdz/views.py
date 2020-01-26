from django.shortcuts import render, get_object_or_404, redirect
from .models import Solution
from django.views.decorators.csrf import csrf_exempt
# from fake_useragent import UserAgent
# import requests
# from bs4 import BeautifulSoup
#
def main_page(request):


    tasks_numbers = Solution.objects.all()
    context = {'tasks': tasks_numbers}
    return render(request, template_name='gdz/main.html', context=context)


def nom_detail(request, number_of_task):
    post = get_object_or_404(Solution, number_of_task=number_of_task)
    next_number = number_of_task + 1
    pre_number = number_of_task - 1
    return render(request, template_name='gdz/detail.html', context={'post': post, 'next_number' : next_number, 'pre_number' : pre_number})


def redirect_page(request):
    return redirect('main-page')

@csrf_exempt
def search_number(request):
    n = request.POST['number']
    print(n)
    try:
        number = Solution.objects.get(number_of_task=n)
        context= {'tasks' : number}
        return render(request, template_name='gdz/search.html', context=context)
    except:
        return render(request, template_name='gdz/search.html')
