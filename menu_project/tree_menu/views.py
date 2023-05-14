from django.shortcuts import render
from django.apps import apps


def index_page(request):
    return render(request, 'tree_menu/index.html')


def get_menu_category(request, model_name, menuitem_id):
    model = apps.get_model(app_label='tree_menu', model_name=model_name)
    content = model.objects.filter(pk=menuitem_id)
    return render(request, 'tree_menu/menu_category.html', {'content': content})

