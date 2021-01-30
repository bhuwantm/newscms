from news.models import NewsCategory
from website.models import Social


def new_context_processor(request):
    category_list = NewsCategory.objects.filter(is_active=True)
    social_links = Social.objects.last()

    return {
        'category_list': category_list,
        'social_links': social_links
    }

