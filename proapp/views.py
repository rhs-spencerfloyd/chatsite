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
    return HttpResponseRedirect(reverse('proapp:results'))


def results(request):
    messages = Message.objects.all().order_by('-id')
    return render(request, "proapp/results.html", {"messages": messages})


def getmessages(request):
    messages = Message.objects.all().order_by('-id').values("message_text")
    messlist = list(messages)
    return JsonResponse(messlist, safe=False)