from django.contrib import admin

from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published') # Список полей, которые видна в админ-панели
    list_display_links = ('id', 'title') # Поля, на которые можно перейти
    search_fields = ('title', 'content') # Поиск информации


admin.site.register(Women, WomenAdmin)
# Register your models here.
