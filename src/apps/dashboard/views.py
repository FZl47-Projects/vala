from django.shortcuts import HttpResponse
from django.views import View
from account.auth.mixins import LoginRequiredMixinCustom


class Index(LoginRequiredMixinCustom, View):

    def get(self,request):
        return HttpResponse('Dashboard')
