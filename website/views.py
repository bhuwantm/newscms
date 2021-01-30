from django.shortcuts import render
from django.views import View

from news.models import News, Tags, NewsCategory, Ads
from website.mixin import GlobalPaginator


class LandingPage(View):
    def get(self, request):
        news_list = News.objects.all()
        headline_list = News.objects.filter(tags__in=Tags.objects.filter(name="Headline"))
        recent_list = News.objects.filter(tags__in=Tags.objects.filter(name="Recent"))
        ads_list = Ads.objects.all()
        return render(request, 'landing.html', {
            'news_list': news_list,
            'headline_list': headline_list,
            'recent_list': recent_list,
            'ads_list': ads_list,
            'is_home': True
        })


class SinglePage(View):
    def get(self, request, pk):
        news = News.objects.get(id=pk, category__is_active=True)
        return render(request, 'single.html', {'news': news})


class CategoryPage(GlobalPaginator, View):
    def get(self, request, pk):
        cat = NewsCategory.objects.get(id=pk, is_active=True)
        all_news_list = cat.cat_news.all().order_by('date')

        page = request.GET.get('page')
        global_paginator = GlobalPaginator()
        paginated_list = global_paginator.get_list(all_news_list, page)

        return render(request, 'category.html', {'news_list': paginated_list, 'cat': cat})
