from django.contrib import admin

from .models import *


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'categories')


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Categories)






