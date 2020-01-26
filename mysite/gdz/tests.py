from .models import Solution
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
def hehe():
    source = requests.get('https://gdz.ru/class-7/algebra/makarychev-uglublennoe-izuchenie/', headers = {'User-Agent' : UserAgent().firefox}).text
    soup = BeautifulSoup(source, 'lxml')
    block = soup.find('section', class_="active")
    numbers = block.div
    for number in numbers.find_all('a'):
        try:
            n = str(number.text)
            t = soup.h1.text
            n = n.replace(' ', '')
            n = n.replace('\t', '')
            n = n.replace('\n', '')
            url = f'https://gdz.ru/class-7/algebra/makarychev-uglublennoe-izuchenie/{n}-nom/'
            print(url)
            source_i = requests.get(url).text
            soup = BeautifulSoup(source_i, 'lxml')
            body = soup.find('body')
            da = body.find('div', class_="with-overtask")
            ia = da.find('img')
            i_url = 'https://' + ia.attrs['src'][2::]
            print(i_url)

            ar = Solution(book=t, number_of_task=n, image=i_url)
            ar.save()
        except :
            print('dont worry')
            continue

def delete():
    q = Solution.objects.all()
    q.delete()
