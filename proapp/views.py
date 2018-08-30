from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils import timezone

from html import escape
from datetime import datetime,timedelta

from .models import Message, IPName, GetRequest

# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    ip = get_client_ip(request)
    try:
        name = IPName.objects.filter(ip=ip)[0].name
    except:
        name = ""
    
    if name != "":
        return render(request, "proapp/index.html")
    else:
        return render(request, "proapp/getname.html", {"ip": ip})


def submit(request):
    post = request.POST.get("textbox")
    if post != "":
        ip = get_client_ip(request)
        message = Message(message_text=escape(post), ip=ip)
        message.save()
        #return [0]
    #return JsonResponse([1, "You cannot send a blank message."], safe=False)
    return HttpResponseRedirect(reverse('proapp:index'))


def setname(request):
    post = request.POST.get("namebox")
    ip = get_client_ip(request)
    ipname = IPName(name=escape(post), ip=ip)
    ipname.save()
    return HttpResponseRedirect(reverse('proapp:index'))


def getmessages(request):
    messages = Message.objects.all().order_by('-id').values()[:20]
    messlist = list(messages)
    for message in messlist:
        try:
            name = IPName.objects.filter(ip=message["ip"])[0].name
        except:
            name = "Unregistered User"
        message["message_text"] = "<b>" + name + "</b>: " + message["message_text"]
        del message["ip"]
        del message["id"]
    return JsonResponse(messlist, safe=False)


def getstats(request):
    ip = get_client_ip(request)
    getrequest = GetRequest(ip=ip, datetime=timezone.now())
    getrequest.save()

    # total number of messages
    nummessages = Message.objects.all().count()

    # users online
    onlineips = GetRequest.objects.filter(datetime__gt=timezone.now()-timedelta(seconds=5))
    online = []
    for oip in onlineips:
        name = IPName.objects.filter(ip=oip.ip)[0].name
        if not(name in online):
            online.append(name)

    # compile statlist
    statlist = {"nummessages": nummessages, "online": sorted(online)}

    return JsonResponse(statlist, safe=False)