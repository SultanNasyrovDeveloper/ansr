from .models import IndexPageTestimonials


def testimonials(request):
    testimonials_set = IndexPageTestimonials.objects.all()
    return testimonials_set

