from django import template
from django.urls import resolve
from menu.models import MenuItem

register = template.Library()

def has_active_child(item, current_url):
    for child in item.children.all():
        if child.url == current_url or has_active_child(child, current_url):
            return True
    return False

@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = resolve(request.path_info).url_name  # Получаем текущий URL
    menu_items = MenuItem.objects.filter(menu__name=menu_name, parent=None)

    def set_active_children(items):
        for item in items:
            item.has_active_child = has_active_child(item, current_url)
            item.is_open = item.url == current_url or item.has_active_child
            set_active_children(item.children.all())

    set_active_children(menu_items)
    return {'menu_items': menu_items, 'current_url': current_url}
