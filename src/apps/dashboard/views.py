from django.shortcuts import render
from django.views import View
from apps.account.auth.mixins import LoginRequiredMixinCustom


class Index(LoginRequiredMixinCustom, View):

    def get(self, request):
        return render(request, 'dashboard/index.html')
