from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Crawl

# Create your views here.

def index(request):
    # return HttpResponse("Hello World")
    crawls = Crawl.objects
    return render(request, 'crawls/index.html', {'crawls':crawls})

def crawl_detail(request,crawl_id):
    crawl = get_object_or_404(Crawl,pk=crawl_id)
    return render(request,'crawls/crawl_detail.html',{'crawl':crawl})

