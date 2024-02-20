from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_channels(paginator:Paginator, page):
    try:
        channels = paginator.page(page)
    except PageNotAnInteger:
        channels = paginator.page(1)
    except EmptyPage:
        channels = paginator.page(paginator.num_pages)
    return channels


def is_exists(model, **kwargs):
    return model.objects.filter(**kwargs).exists()