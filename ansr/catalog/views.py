import random

from django.shortcuts import render, get_object_or_404

from ansr.core.views import AnsarView
from ansr.index.models import IndexPageTestimonials
from ansr.core.models import SiteSettings
from ansr.callback.forms import CallbackForm

from .models import Product, ProductAdvantage


def get_recommendations(current):
    ids = list(Product.objects.exclude(id=current).values_list('id', flat=True))
    if len(ids) > 7:
        target_ids = random.sample(ids, 7)
    else:
        target_ids = ids
    return Product.objects.filter(id__in=target_ids)


class ProductsList(AnsarView):
    def get(self, request, *args, **kwargs):
        context = dict()
        context['products'] = Product.objects.all()
        return render(request, 'catalog/product-list.html', context)


class ProductDetail(AnsarView):
    def get(self, request, *args, **kwargs):
        target = get_object_or_404(Product, id=kwargs['product_id'])
        context = dict()
        context['target'] = target
        context['testimonials'] = IndexPageTestimonials.objects.all()
        context['form'] = CallbackForm()
        context['recommendations'] = get_recommendations(int(kwargs['product_id']))
        context['advantages'] = ProductAdvantage.objects.all()
        try:
            context['site_settings'] = SiteSettings.objects.get()
        except SiteSettings.DoesNotExist:
            context['site_settings'] = {}
        return render(request, 'catalog/detail.html', context)
