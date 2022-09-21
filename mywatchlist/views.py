from cgitb import html
from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist_html(request):
    film_item = MyWatchList.objects.all()
    context = {
        'list_film': film_item,
        'nama': 'Vinsensius Ferdinando',
        'npm': '2106751221'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def check_total(request):
    data = MyWatchList.objects.all()
    total_watched = 0
    total_unwatched = 0
    for film in data:
        if film.watched == "Yes":
            total_watched+=1
        else:
            total_unwatched+=1
    status = ""
    if(total_watched >= total_unwatched):
        status = "Selamat, kamu sudah menonton banyak!"
    else:
        status = "Wah, kamu masih sedikit menonton!"

    context = {
        'nama': 'Vinsensius Ferdinando',
        'npm': '2106751221',
        'status': status,
    }
    return render(request, "total.html", context)
    
    