from django.contrib import admin

# Register your models here.
from .models import Categorie, Article

admin.site.register(Categorie)


class ArticleAdmin(admin.ModelAdmin):
   list_display   = ('titre', 'auteur', 'date')
   list_filter    = ('auteur','categorie',)
   date_hierarchy = 'date'
   ordering       = ('date', )
   search_fields  = ('titre', 'contenu')

admin.site.register(Article, ArticleAdmin)
