import re
from pprint import pprint
import wikipedia
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views import View
import requests
from bs4 import BeautifulSoup
import requests
import os
# from urllib import request
# import urllib
# Create your views here.
from dateutil.parser import parse

class NewsList(View):

    @staticmethod
    def grab_page(url):
        # news = urllib.request.urlopen('http://www.wdylike.appspot.com/?q=')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }

        news = requests.get(url, headers=headers)
        return news

    @staticmethod
    def fetch_content(base_link, directory='', html=''):
        snippets = []
        if html == '':
            link = base_link + directory
            news = NewsList.grab_page(link)
            soup = BeautifulSoup(news.content, 'html.parser')

            news = soup.find('div', {'td-ss-main-content'})
            all_news = news.find_all('div', {'td-block-span6'})

            news2 = """
                    
                    <a href="http://www.szczecinek.org/images/mapy/prusy1881.JPG" target="_blank" rel="noopener" data-rel="lightbox-image-4" data-rl_title="" data-rl_caption="" title="">MAPA PROWINCJI PRUS WSCHODNICH I ZACHODNICH Z 1881 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/prusy1886.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-5" data-rl_title="" data-rl_caption="" title="">MAPA PRUS WSCHODNICH I ZACHODNICH Z 1886 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/pomerania.JPG" target="_blank" rel="noopener" data-rel="lightbox-image-6" data-rl_title="" data-rl_caption="" title="">MAPA POMORZA OK. 1890 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/58081158.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-7" data-rl_title="" data-rl_caption="" title="">MAPA POMORZA Z 1890 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/57917268.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-8" data-rl_title="" data-rl_caption="" title="">MAPA POMORZA Z 1890 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/55165850.jpg" data-rel="lightbox-image-9" data-rl_title="" data-rl_caption="" title="">MAPA POMORZA  Z KOŃCA XIX WIEKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/administracyjna1897.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-10" data-rl_title="" data-rl_caption="" title="">MAPA ADMINISTRACYJNA PÓŁNOCNYCH NIEMIEC Z 1897 ROKU</a></p>
                    <p><span style="font-size: 12pt;"><strong>Okres niemiecki &#8211; do 1945 r.</strong></span></p>
                    <p><a href="http://www.szczecinek.org/images/mapy/58090960.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-11" data-rl_title="" data-rl_caption="" title="">MAPA KOLEJOWA PÓŁNOCNYCH NIEMIEC Z 1925 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/kolej1928.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-12" data-rl_title="" data-rl_caption="" title="">FRAGMENT MAPY KOLEJOWEJ POMORZA Z 1928 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/mapa_kolei_1944.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-13" data-rl_title="" data-rl_caption="" title="">MAPA SIECI KOLEJOWEJ NA POMORZU W 1944 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/Map3aSW.pdf" target="_blank" rel="noopener" title="">MAPA POMORZA I KUJAW Z POCZĄTKU XX WIEKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/pommern.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-14" data-rl_title="" data-rl_caption="" title="">MAPA POMORZA OK. 1900 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/43898546.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-15" data-rl_title="" data-rl_caption="" title="">MAPA PROWINCJI POMORZA Z 1900 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/wojsko1901.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-16" data-rl_title="" data-rl_caption="" title="">MAPA ROZMIESZCZENIA GARNIZONÓW W EUROPIE ŚRODKOWEJ Z 1901 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/branderburgia1902.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-17" data-rl_title="" data-rl_caption="" title="">MAPA BRANDENBURGII Z 1902 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/deutsches_reich_1_3700000.pdf" target="_blank" rel="noopener" title="">MAPA CAŁYCH NIEMIEC Z POMORZEM Z ROKU 1905</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/POMORZE_GDAŃSKIE1911.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-18" data-rl_title="" data-rl_caption="" title="">MAPA POMORZA GDAŃSKIEGO Z 1911 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/deutsches-reich_1917.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-19" data-rl_title="" data-rl_caption="" title="">MAPA NIEMIEC Z 1917 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/wschodnieprus1919.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-20" data-rl_title="" data-rl_caption="" title="">MAPA PRUS WSCHODNICH Z 1919 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/edukacyjne.htm" target="_blank" rel="noopener" title="">MAPKI EDUKACYJNE POMORZA Z 1925 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/posen.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-21" data-rl_title="" data-rl_caption="" title="">MAPA WIELKOPOLSKI Z POCZĄTKU XX WIEKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/48652271.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-22" data-rl_title="" data-rl_caption="" title="">MAPA POMORZA Z 1933 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/pom1935.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-23" data-rl_title="" data-rl_caption="" title="">MAPA POMORZA I BRANDERBURGII Z 1935 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/01_III_RZESZA_1942_GAUEINTEILUNG.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-24" data-rl_title="" data-rl_caption="" title="">MAPA III RZESZY NIEMIECKIEJ Z 1942 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/03_III_RZESZA_1942_POMORZE_GDANSK.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-25" data-rl_title="" data-rl_caption="" title="">MAPA POMORZA GDAŃSKIEGO Z 1942 ROKU</a></p>
                    <p><strong><span style="font-size: 12pt;">Okres PRL &#8211; lat 1945-1989</span></strong></p>
                    <p><a href="http://www.szczecinek.org/images/mapy/kolej_pomorza.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-26" data-rl_title="" data-rl_caption="" title="">MAPA SIECI KOLEJOWEJ NA POMORZU Z MARCA 1946 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/31_PomorskieKD.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-27" data-rl_title="" data-rl_caption="" title="">SCHEMATYCZNA MAPKA SIECI KOLEI WĄSKOTOROWEJ NA POMORZU PO 1945</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/mapa_pkd.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-28" data-rl_title="" data-rl_caption="" title="">MAPA SIECI KOLEI WĄSKOTOROWEJ NA POMORZU Z LAT CZTERDZIESTYCH</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/1966.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-29" data-rl_title="" data-rl_caption="" title="">MAPA SIECI KOLEJOWEJ POMORZA Z 1966 ROKU</a><br />
                    <a href="http://www.szczecinek.org/images/mapy/mapa_kolei.jpg" target="_blank" rel="noopener" data-rel="lightbox-image-30" data-rl_title="" data-rl_caption="" title="">SCHEMATYCZNA MAPA SIECI KOLEJOWEJ POMORSKIEJ DOKP Z 1979 ROKU</a>

                """


            for item in all_news:
                snippets.append([
                    parse(item.time['datetime']),
                    item.a['title'],
                    base_link + item.a['href'],
                    base_link + item.img['src'],
                ])
        else:
            news = html
            soup = BeautifulSoup(news)
            all_news = soup.find_all('a')

            for item in all_news:

                snippets.append([
                    item.text,
                    item.attrs['href']
                ])


    # all_news2 = [queryset.add(item) for item in list_of_links]

        # snippets.sort(reverse=True)
        return snippets

    def get(self, request):

        # __snippets = self.fetch_news('https://kurierkolejowy.eu', '/wiadomosci')
        # print(__snippets)
        ctx = {
            # 'snippets': __snippets,

        }

        return render(request, 'news_module.html', ctx)






# class WikipediaObject(View):
#     def get(self, request):
#
#
#         ctx = {
#             'snippets': snippets,
#
#         }
#
#         return render(request, 'news.html', ctx)