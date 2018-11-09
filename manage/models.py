from django.db import models

from publishing.models import Article, Category


class ArtList(models.Model):
     #menu = Category.objects.filter(parent_id=70)
     positions = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='position', null=True, limit_choices_to={'parent_id': 70})
     artlist = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article', null=True)

     def __str__(self):
         return self.artlist.title
     class Meta:
        verbose_name = "Lista artykułów"
        verbose_name_plural = "Lista artykułów"

#
class LeftColumn(models.Model):
    class Meta:
        verbose_name = "Lewa Kolumna"
        verbose_name_plural = "Lewa Kolumna"
#
# class RightColumn(models.Model):
#     class Meta:
#         verbose_name = "Prawa Kolumna"
#         verbose_name_plural = "Prawa Kolumna"