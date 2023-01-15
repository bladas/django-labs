from django.contrib import admin
from blog.forms import CategoryForm
from blog.models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    fieldsets = (('', {'fields': ('category', 'slug'), }),)
    prepopulated_fields = {'slug': ('category',)}
    form = CategoryForm


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page')
    multiupload_form = True
    multiupload_list = False
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('category',)
    fieldsets = (('', {'fields': ('pub_date', 'title', 'description', 'main_page'), }),
                 (('Додатково'), {'classes': ('grp-collapse grp-closed',), 'fields': ('slug',), }),)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
