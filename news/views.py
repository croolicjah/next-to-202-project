import re
from pprint import pprint
import wikipedia
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views import View
import requests
from bs4 import BeautifulSoup
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
    def fetch_news(base_link, directory):

        link = base_link + directory
        news = NewsList.grab_page(link)
        soup = BeautifulSoup(news.content, 'html.parser')

        news = soup.find('div', {'td-ss-main-content'})
        all_news = news.find_all('div', {'td-block-span6'})

        snippets = []
        for item in all_news:
            snippets.append([
                parse(item.time['datetime']),
                item.a['title'],
                base_link + item.a['href'],
                base_link + item.img['src'],
            ])

        # snippets.sort(reverse=True)
        return snippets

    def get(self, request):

        # __snippets = self.fetch_news('https://kurierkolejowy.eu', '/wiadomosci')
        # print(__snippets)
        # ctx = {
        #     'snippets': __snippets,
        #
        # }

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