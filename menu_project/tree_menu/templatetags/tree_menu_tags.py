from django import template
from django.apps import apps
from tree_menu.models import MainMenu

register = template.Library()

@register.inclusion_tag('tree_menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    path = context['request'].path
    model = apps.get_model(app_label='tree_menu', model_name=menu_name)
    queryset = model.objects.all()
    return {'menu': queryset, 'path': path, 'menu_name': menu_name}
