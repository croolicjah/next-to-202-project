from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views import View

from news.views import NewsList
from .models import Photo, Article
from .forms import AddPhotoForm


# Create your views here.
class MainPage(View):

    def get(self, request):

        # prepare middle column with articles list
        posts = Article.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')

        __snippets = NewsList.fetch_news('https://kurierkolejowy.eu', '/wiadomosci')
        # self.LayoutPrepare() -> ctx set
        # print(posts.values())
        #post = Article.objects.get(pk=1)
        # main_media = Photo.objects.get(pk=1)

        #prepare left column


        #prepare right column


        #add app


        ctx = {
            # 'photo': main_media,
            'snippets' : __snippets,
            'posts': posts
        }
        return render(request, 'index.html', ctx)

    def post(self, request):
            post = Article.objects.get(pk=1)

            return HttpResponse("Powrót")

class MapsGalleryView(View):
    pass


class SingleArticleView(View):
    def get(self, request, id):
        article = Article.objects.get(id=id)

        ctx = {
            'article' : article,

        }

        return render(request, 'single.html', ctx)

    def post(self, request):
        form = AddPhotoForm(request.POST, request.FILES)
        photos = Photo.objects.all().order_by('-id')

        if form.is_valid():
            form.save()
            return render(request, 'add_image.html', {'photos': photos})
        else:
            return render(request, 'add_image.html', {'form': form})


class AddImageViewDev(View):
    def get(self, request):
        photos = Photo.objects.all()
        form = AddPhotoForm()
        ctx = {
            'photos' : photos,
            'form' : form
        }

        return render(request, 'add_image.html', ctx)

    def post(self, request):
        form = AddPhotoForm(request.POST, request.FILES)
        photos = Photo.objects.all().order_by('-id')

        if form.is_valid():
            form.save()
            return render(request, 'add_image.html', {'photos': photos})
        else:
            return render(request, 'add_image.html', {'form': form})