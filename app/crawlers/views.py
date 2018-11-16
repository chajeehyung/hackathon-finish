from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests


def image_search(request):
    search_keyword = request.GET.get('search_keyword')
    # return redirect('image_list', search_keyword)
    return image_list(request,search_keyword)

def image_list(request, search_keyword=''):
    url_prefix = 'https://www.google.co.kr/search?q='
    url_surfix = '&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjqzdHerNbeAhXGW7wKHaNYCykQ_AUIDigB&biw=1853&bih=950'
    url = url_prefix + search_keyword + url_surfix

    response = requests.get(url)
    open('pby.html', 'wt').write(response.text)
    html = open('pby.html', 'rt').read()
    soup = BeautifulSoup(html, 'lxml')
    col_list = soup.find_all('img')
    urls = []
    for col in col_list:
        urls.append(col.get('src'))

    context = {
        'urls': urls
    }

    return render(request, 'posts/post_list.html', context)
