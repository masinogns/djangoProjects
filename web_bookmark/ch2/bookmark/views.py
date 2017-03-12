from django.shortcuts import render, render_to_response

# Create your views here.
from bookmark.models import Bookmark
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    return HttpResponse("<h1>Web page is Success</h1>")

def list(request):
    bookmarks = Bookmark.objects.all()
    return render(request, "bookmark/list.html", {"bookmarks": bookmarks})
    # return HttpResponse("<p>zzzz</p>")

def detail(request, bookmarkkey):
    #lotto = GuessNumbers.objects.get(pk=lottokey)
    bookmark = Bookmark.objects.get(pk=bookmarkkey)
    return render(request, "bookmark/detail.html", {"bookmark": bookmark})
