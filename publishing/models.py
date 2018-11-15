from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
# from filer.fields.file import FilerFileField
# from filer.fields.image import FilerImageField
from django.utils.safestring import mark_safe
from embed_video.fields import EmbedVideoField
from ckeditor_uploader.fields import RichTextUploadingField
import requests
import os


PRODUCTION_STATUS = (
    (1, "w trakcie"),
    (2, "do akceptacji"),
    (3, "gotowy do publikacji"),
    (4, "opublikowany")
)





class Category(models.Model):
    name = models.CharField(max_length=64)
    number = models.IntegerField(null=True)
    visible = models.BooleanField(null=True, blank=True, name="visible")
    parent_id   = models.IntegerField(null=True)
    # models.ManyToManyField('Article', related_name='category_article')

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo = models.ImageField(max_length=255, name="photo")
    caption = RichTextField(config_name='simple_toolbar', max_length=255, blank=True, null=True)
    author = models.CharField(max_length=64, blank=True, null=True)
    source = models.CharField(max_length=20, blank=True, null=True)
    article = models.ForeignKey('Article', on_delete=models.CASCADE, blank=True, null=True)

    def image_tag(self):
        if self.photo:
            image = mark_safe('<img src="/media/%s" width="640" />' % (self.photo))
        else:
            image = mark_safe('<img src="/media/zaladuj.png" width="640" />')
        return image

    image_tag.short_description = 'Image'

    # def image_thumb(self):
    #     return mark_safe('<img src="/media/%s" width="100" height="100" />') % (self.photo)
    #
    # image_thumb.allow_tags = True

    def __str__(self):
        return str(self.photo)

    # likes = models.ManyToManyField(MyUser)


class Video(models.Model):
    video = EmbedVideoField()
    source = models.CharField(max_length=20, blank=True, null=True)
    article = models.ForeignKey('Article', on_delete=models.CASCADE, blank=True, null=True, name='video_article')


class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    # lead = models.TextField(max_length=765, null=True)
    # text = models.TextField(blank=True, null=True)
    lead = RichTextField(config_name='lead', max_length=765, null=True)
    text = RichTextUploadingField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=False, blank=True, name="active")
    categories = models.ManyToManyField('Category', related_name='categories')
    #main_multimedia2 = FilerFileField(related_name='zdjecia')

    status = models.IntegerField(choices=PRODUCTION_STATUS, default=1)

    # metoda sprawi, że w widoku listy artykułów pojawi się typ: galerry, article...
    def spice(self):
        return ",".join([str(p) for p in self.categories.filter(parent_id=200)])

    # def get_visibility(self):
    #     return ",".join([str(p) for p in self.categories.filter(visible__isnull=False)])

    spice.short_description = 'type'
    # spice.admin_order_field = 'categories'
    def publish(self):
        self.publish_date = timezone.now()
        # self.update_date = self.publish_date
        # self.status = 4
        self.save()

    def update(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Gallery(Article):
    pass


# class Snippet(models.Models):
#     start_emission = models.DateField(null=True)
#     stop_emission = models.DateField(null=True)
#
#
#
#     def set_visible(self, start_emmision, stop_emission, site_position=0, inmodule_position=0):
#         self.start_emission = timezone.now()
#         self.save()
#         return (site_position, inmodule_position)
#
#     def set_unvisible(self):
#         self.stop_emission = timezone.now()
#         self.save()
#         return False



class Comment(models.Model):
    signalist = models.CharField(max_length=32, null=True)
    content = models.TextField(null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)




# class ArticleS(models.Model):
#     title = models.CharField(max_length=128)
#     author = models.CharField(max_length=64)
#     content = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#
#     category = models.ManyToManyField(Category)
#
#     def __str__(self):
#         return "{}, {}".format(self.title, self.author)

POSITIONS = {
    1: 'header',
    2: 'bottom_header_ad',
    3: 'top_ad',
    4: '',
}

# class Layout(models.Model)