from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class GlobalPaginator(object):

    def __init__(self, page_capacity=12):
        self.page_capacity = page_capacity


    def get_list(self, all_lst, page):
        paginator = Paginator(all_lst, self.page_capacity)
        try:
            page_lst = paginator.page(page)
        except PageNotAnInteger:
            page_lst = paginator.page(1)
        except EmptyPage:
            page_lst = paginator.page(paginator.num_pages)

        return page_lst