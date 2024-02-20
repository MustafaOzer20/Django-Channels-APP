from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_page_data(paginator:Paginator, page):
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return data


def is_exists(model, **kwargs):
    return model.objects.filter(**kwargs).exists()