from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import City
# Create your views here.

def index(request):

    return render(request, 'mysearchapp/index.html')


def search(request):
    search=[]
    search_recv = request.GET.get('term')
    search_results = City.objects.filter(name__icontains=search_recv)
    for result in search_results:
        search.append(result.name)
    return JsonResponse(search, safe=False)
