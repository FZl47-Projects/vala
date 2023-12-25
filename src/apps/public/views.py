from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'public/index.html'


def err_403_handler(request, exception):
    return render(request, 'public/errors/page-error-403.html')


def err_404_handler(request, exception):
    return render(request, 'public/errors/page-error-404.html')


def err_500_handler(request):
    return render(request, 'public/errors/page-error-500.html')
