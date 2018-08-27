from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

from .models import Message

# Create your views here.

def index(request):
    return render(request, "proapp/index.html")


def submit(request):
    post = request.POST.get("textbox")
    message = Message(message_text=post)
    message.save()
    return HttpResponseRedirect(reverse('proapp:index'))


def getmessages(request):
    messages = Message.objects.all().order_by('-id').values("message_text")[:20]
    messlist = list(messages)
    return JsonResponse(messlist, safe=False)