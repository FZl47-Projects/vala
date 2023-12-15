from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from django.shortcuts import redirect, reverse


# Render Index view
class IndexView(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
        pass
