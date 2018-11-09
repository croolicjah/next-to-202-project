from django.contrib import admin

# Register your models here.
from .models import ArtList
from publishing.admin import ArticleAdmin
from publishing.models import Category, Article


@admin.register(ArtList)
class ArtListAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "positions":
            kwargs["queryset"] = Category.objects.order_by('number')
        return super(ArtListAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('artlist', 'positions',)

