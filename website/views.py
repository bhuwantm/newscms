from django.shortcuts import render
from django.views import View

from news.models import News, Tags, NewsCategory, Ads
from website.mixin import GlobalPaginator


class LandingPage(View):
    def get(self, request):
        news_list = News.objects.all()
        headline_list = News.objects.filter(tags__in=Tags.objects.filter(name="Headline"))
        recent_list = News.objects.filter(tags__in=Tags.objects.filter(name="Recent"))
        pinned_list = News.objects.filter(tags__in=Tags.objects.filter(name="Pinned"))
        ads_list = Ads.objects.all()
        return render(request, 'landing.html', {
            'news_list': news_list,
            'headline_list': headline_list,
            'pinned_list': pinned_list,
            'recent_list': recent_list,
            'ads_list': ads_list
        })


class SinglePage(View):
    def get(self, request, pk):
        news = News.objects.get(id=pk)
        return render(request, 'single.html', {'news': news})


class CategoryPage(GlobalPaginator, View):
    def get(self, request, pk):
        cat = NewsCategory.objects.get(id=pk)
        all_news_list = cat.cat_news.all().order_by('date')

        page = request.GET.get('page')
        global_paginator = GlobalPaginator()
        paginated_list = global_paginator.get_list(all_news_list, page)

        return render(request, 'category.html', {'news_list': paginated_list})
