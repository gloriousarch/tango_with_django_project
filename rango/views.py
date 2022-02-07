from django.shortcuts import render

from rango.models import Category, Page


def index(request):
    categories = Category.objects.order_by('-likes')[:5]
    pages = Page.objects.order_by('-views')[:5]

    context = dict()
    context['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context['categories'] = categories
    context['pages'] = pages

    return render(request, 'rango/index.html', context=context)


def about(request):
    return render(request, 'rango/about.html')


def show_category(request, category_name_slug):
    context = dict()

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context['pages'] = pages
        context['category'] = category
    except Category.DoesNotExist:
        context['category'] = None
        context['pages'] = None

    return render(request, 'rango/category.html', context=context)
