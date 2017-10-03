from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib2


# Create your views here.
def index(request):
    url = "https://api.data.gov.in/resource/0a076478-3fd3-4e2c-b2d2-581876f56d77?format=json&api-key=579b464db66ec23bdd000001d15d144d27ca4c3b702b8a67f865eb17"
    posturi = url + "&filters[pincode]=44190*"

    proxy = urllib2.ProxyHandler({'https':"http://mvineet:Ampersand&7@proxy.barc.gov.in:8080"})
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
    urllib2.install_opener(opener)


    response = urllib2.urlopen(posturi)

#print response
    jsonresponse =  json.load(response)

    return HttpResponse(json.dumps(jsonresponse, indent=4))
    
    # return HttpResponse("Hello!")


def get_postal_data(request):
    pass

