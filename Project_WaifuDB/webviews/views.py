from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from Project_WaifuDB.assets.models import Waifu, WaifuAssetFileStorage, WaifuAssetClientPicture


class IndexView(generic.ListView):
    template_name = "website/index.html"
    context_object_name = "latest_waifu_list"

    def get_queryset(self):
        return Waifu.objects.order_by("-date_uploaded")[:10]


class DetailView(generic.DetailView):
    model = Waifu
    template_name = "website/detail.html"



