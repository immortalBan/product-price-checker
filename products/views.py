from django.shortcuts import render
from . import parse_query


def index(request):
    return render(request, 'index.html', {'title': 'Главная страница'})


def about_us(request):
    return render(request, 'about.html')


def search(request):
    query = request.GET.get('searchbox')
    object_list = parse_query.parse_request(query)
    return render(request, 'search.html', {'title': 'Поиск', 'body': query, 'object_list': object_list})


def product_view(request):
    product = request.GET.get('product')
    query = request.GET.get('query')
    object_list, picture_url = parse_query.parse_product(product, query)
    description, structure = parse_query.parse_structure(product, query)
    return render(request, 'product_view.html', {'title': product, 'body': product, 'object_list': object_list,
                                                 'picture_url': picture_url, 'description': description, 'structure': structure})
