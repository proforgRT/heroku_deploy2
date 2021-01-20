from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View

from .models import Men


class MenView(View):
    def get(self, request):
        mens = Men.objects.all()
        return render(request, "mens/mens_list.html", {"mens_list": mens})


class MenDetailView(View):
    def get(self, request, pk):
        men = Men.objects.get(id=pk)
        return render(request, "mens/mens_detail.html", {"men": men})