## Create your views here.
#from django.shortcuts import HttpResponse
#from django.conf import Settings
#from django.template import RequestContext, Template, Context
#from Project_WaifuDB.assets.models import Waifu, WaifuAssetProfilePicture
#import django.core.context_processors
#
#def imageview(request):
#    html = Template('<img src="{{MEDIA_URL}}" style="img{ max-width:100px}"/>')
#    ctx = {'MEDIA_URL':django.core.context_processors.media}
#    return HttpResponse(html.render(Context(ctx)))