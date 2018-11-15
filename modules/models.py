from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
import requests
import os
from bs4 import BeautifulSoup
# Create your models here.
from publishing.models import Photo, Article
from publishing.views import NewsList
from django.conf import settings


class GalleryWizard(Article):

    # html = models.TextField()

    @staticmethod
    def save_images(html):
        __urls = []
        links = NewsList.fetch_content('', '', html)

        invalid_name = True
        # directoryname = links.split('.')
        directory = links[0][1].split('/')
        while invalid_name:
            if not os.path.exists(settings.MEDIA_ROOT + '/'  + directory[2]):
                os.makedirs(settings.MEDIA_ROOT + '/' + directory[2])
                break
            directory[2] += '1'
        for url in links:
            filename = url[1].split('/')[-1]
            r = requests.get(url[1], allow_redirects=True)
            open(settings.MEDIA_ROOT + '/'  + directory[2] + '/' + filename, 'wb').write(r.content)
            __urls.append([f"{url[0]}", directory[2] + '/' + filename])
        return __urls


    def make_gallery(self, html):

        return None
