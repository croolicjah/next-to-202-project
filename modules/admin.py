from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.contrib.gis.db import models
# from mapwidgets.widgets import GooglePointFieldWidget
#
#
# class CityAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.PointField: {"widget": GooglePointFieldWidget}
#     }
from django.forms import TextInput, SelectMultiple, Textarea

from modules.models import GalleryWizard


@admin.register(GalleryWizard)
class GalleryWizzardAdmin(admin.ModelAdmin):
    exclude= ('text',)

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '99'})},


        models.TextField: {'widget': Textarea(attrs={'cols': '132'})},
    }

    def save_model(self, request, obj, form, change):


        obj.save()
        photos = GalleryWizard.save_images(request.POST.get('html1'))
        print(photos[0][0])

        for item in photos:

            obj.photo_set.create(photo=item[1], caption=item[0])

