from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', context=None)
