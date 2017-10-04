from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import json
import urllib2


# Create your views here.
def index(request):
    #return HttpResponse(template.render(context, request))
    return render(request, "podata/index.html")
    


def get_postal_data(request):
    post_request = request.POST

    posturi = "https://api.data.gov.in/resource/0a076478-3fd3-4e2c-b2d2-581876f56d77?format=json&api-key=579b464db66ec23bdd000001d15d144d27ca4c3b702b8a67f865eb17"
    # posturi = posturi + "&filters[pincode]=441906"

    proxy = urllib2.ProxyHandler({'https':"http://mvineet:Ampersand&7@proxy.barc.gov.in:8080"})
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    response = urllib2.urlopen(posturi)

    jsonresponse =  json.load(response)
    print json.dumps(jsonresponse, indent=4)

    datatable_response = {
        'draw': int(post_request.get("draw")), 
        'recordsTotal': jsonresponse.get("total"), 
        'recordsFiltered': jsonresponse.get("count"), 
        'data': jsonresponse.get('records')
    }

    return JsonResponse(datatable_response)
