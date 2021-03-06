"""next202 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from publishing.views import MainPage, AddImageViewDev, SingleArticleView, MapsGalleryView
from django.conf import settings
from django.conf.urls.static import static
from modules.views import NewsList
from filebrowser.sites import site



urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('jet/', include('jet.urls', 'jet')),  #('grappelli/', include('grappelli.urls')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name='article-list'),
    path('news/', NewsList.as_view(), name='news'),
    path('image/', AddImageViewDev.as_view(), name="add-image'"),
    path('maps/', MapsGalleryView.as_view(), name="maps'"),
    re_path(r'^\D-(?P<article_id>(\d)+)/$', SingleArticleView.as_view(), name="single_article"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     url('admin/', admin.site.urls),
#     url('', ArticleList.as_view(), name='article-list'),
#     url('image/', AddImageViewDev.as_view(), name="add-image'"),
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
