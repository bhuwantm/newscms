from django.shortcuts import render
from django.shortcuts import render
from django.views import View

from news.models import News, NewsCategory, Ads
from website.mixin import GlobalPaginator


class LandingPage(View):
    def get(self, request):
        news_list = News.objects.all().order_by('-date')[:4]

        headline_list = News.objects.filter(tags__name="Headline")[:4]
        headline_list_pinned = News.objects.filter(tags__name="Headline").filter(tags__name="Pinned")

        recent_list = News.objects.filter(tags__name="Recent")[:4]
        recent_list_pinned = News.objects.filter(tags__name="Recent").filter(tags__name="Pinned")

        ads_list = Ads.objects.all()
        return render(request, 'landing.html', {
            'news_list': news_list,
            'headline_list': headline_list,
            'headline_list_pinned': headline_list_pinned,
            'recent_list': recent_list,
            'recent_list_pinned': recent_list_pinned,
            'ads_list': ads_list,
            'is_home': True
        })


class SinglePage(View):

    def post(self, request, pk):
        # use of api is highly recommended for this type of post
        news = News.objects.get(id=pk, category__is_active=True)
        if 'like' in request.POST:
            news.likes_counter += 1
            news.save()
        return render(request, 'single.html', {'news': news})

    def get(self, request, pk):
        news = News.objects.get(id=pk, category__is_active=True)
        news.views_counter += 1
        news.save()
        return render(request, 'single.html', {'news': news})


class CategoryPage(GlobalPaginator, View):
    def get(self, request, pk):
        cat = NewsCategory.objects.get(id=pk, is_active=True)
        all_news_list = cat.cat_news.all().order_by('date')

        page = request.GET.get('page')
        global_paginator = GlobalPaginator()
        paginated_list = global_paginator.get_list(all_news_list, page)

        return render(request, 'category.html', {'news_list': paginated_list, 'cat': cat})
