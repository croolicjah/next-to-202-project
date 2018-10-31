from django.contrib import admin
from .models import Article, Photo
# Register your models here.
# admin.site.register(Article)
# admin.site.register(Photo)


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.photo.create(article=afile)


admin.site.register(Article, ArticleAdmin)