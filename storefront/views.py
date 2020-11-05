from django.shortcuts import render
from django.views.generic import DetailView
from storefront.models import Store, Category

def index_page(request):
    item = Store.objects.all()
    context = {
        'item': item
        }
    return render(request, 'index_page.html', context)

def storefront_index(request):
    item = Store.objects.all()
    context = {
        'item': item,
        }
    return render(request, 'storefront_index.html', context)

def storefront_detail(request, pk):
    item = Store.objects.get(pk=pk)
    context = {
        'item': item
        }
    return render(request, 'storefront_detail.html', context)

def storefront_category(request, category):
    item = Store.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-categories'
    )
    context = {
        "category": category,
        "item": item
    }
    return render(request, "storefront_category.html", context)
