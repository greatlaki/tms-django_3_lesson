<<<<<<< HEAD
from django.db.models.aggregates import Count
from django.core.cache import caches
=======
>>>>>>> origin

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'}, # index 1
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

class DataMixin:
<<<<<<< HEAD
        paginate_by = 3 # Количесвто элементов списка на страницу

=======
>>>>>>> origin
        def get_user_conext(self, **kwargs):
                context = kwargs
                cats = Category.objects.annotate(Count('women'))

                user_menu = menu.copy()
                if not self.request.user.is_authenticated:
                        user_menu.pop(1)

                context['menu'] = user_menu

                context['cats'] = cats
                if 'cat_selected' not in context:
                        context['cat_selected'] = 0
                return context