from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views import View
from .models import Photo, Article
from .forms import AddPhotoForm


# Create your views here.
class ArticleList(View):

    def get(self, request):
        posts = Article.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
        # print(posts.values())
        #post = Article.objects.get(pk=1)
        # main_media = Photo.objects.get(pk=1)



        ctx = {
            # 'photo': main_media,
            'posts': posts
        }
        return render(request, 'index.html', ctx)

    def post(self, request):
            post = Article.objects.get(pk=1)

            return HttpResponse("Powrót")


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