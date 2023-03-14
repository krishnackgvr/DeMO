from .models import place, Item

from django.shortcuts import render


# Create your views here.
def demo(request):
    obj = place.objects.all()
    item = Item.objects.all()
    return render(request, "index.html", {'result': obj, 'item': item})
