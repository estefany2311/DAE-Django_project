from django.shortcuts import render

from .models import Item


def item_list(request):
	items = Item.objects.all()
	return render(request, 'core/item_list.html', {'items': items})
from django.http import JsonResponse

def item_list_api(request):
    items = list(Item.objects.values('id', 'name', 'description', 'created_at'))
    return JsonResponse(items, safe=False)
