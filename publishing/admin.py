from django.contrib import admin
from .models import Article, Photo, Video
# Register your models here.
# admin.site.register(Article)
# admin.site.register(Photo)


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    inlines = [PhotoInline]

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):

            obj.photo_set.create(article=afile)
