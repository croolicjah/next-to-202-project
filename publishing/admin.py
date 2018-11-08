from django.contrib import admin
from jet.admin import CompactInline

from .models import Article, Photo, Video, Category


# Register your models here.
# admin.site.register(Article)
# admin.site.register(Photo)
# admin.StackedInline

class PhotoInline(CompactInline):
    model = Photo
    extra = 1
    show_change_link = True

# class CategoriesInline(admin. TabularInline):
#     model = Category.article.through



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # def get_visibilityl(self, obj):
    #     return obj..country_code.label)

    list_display = ("title", 'spice', "author", "active", "status", "create_date", "publish_date")
    # list_filter = ["categories"]
    search_fields = ['categories', 'title']
    inlines = [PhotoInline]
    # filter_horizontal = ("article",)
    # fields = ('title', 'category_article',)

    # exclude = ['article']
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "categories":
            kwargs["queryset"] = Category.objects.filter(number__gt=200)
            print(kwargs["queryset"])
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):


        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):

            obj.photo_set.create(article=afile)



# You may not be able to do it directly. From the documentation of list_display
#
# ManyToManyField fields aren’t supported, because that would entail executing a separate SQL statement for each row in the table. If you want to do this nonetheless, give your model a custom method, and add that method’s name to list_display. (See below for more on custom methods in list_display.)
#
# You can do something like this:
#
# class PurchaseOrderAdmin(admin.ModelAdmin):
#     fields = ['product', 'dollar_amount']
#     list_display = ('get_products', 'vendor')
#
#     def get_products(self, obj):
#         return "\n".join([p.products for p in obj.product.all()])
# OR define a model method, and use that
#
# class PurchaseOrder(models.Model):
#     product = models.ManyToManyField('Product')
#     vendor = models.ForeignKey('VendorProfile')
#     dollar_amount = models.FloatField(verbose_name='Price')
#
#     def get_products(self):
#         return "\n".join([p.products for p in self.product.all()])
# and in the admin list_display
#
# list_display = ('get_products', 'vendor')