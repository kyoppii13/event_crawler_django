from django.shortcuts import render
from django.http import HttpResponse
from crawls.models import ScrapyItem
from scrapyd_api import ScrapydAPI
import datetime
import csv
import io
from crawls.test import MyCalendar
from django.utils.safestring import mark_safe

# Create your views here.
scrapyd = ScrapydAPI('http://localhost:6800')

from django.views import generic
from scalendar.views import MonthCalendarMixin

def top(request, month=None, year=None):
    # if request.method == 'POST':
    #     url = request.POST.get('url')
    # return render(request, 'crawls/index.html')
    if month is None and year is None:
        today = datetime.datetime.today()
        month = today.month
        year = today.year

    date = datetime.datetime.now()

    my_calendar = MyCalendar()
    my_calendar_html = my_calendar.formatmonth(2018, 4)
    result_html = mark_safe(my_calendar_html)

    crawls = ScrapyItem.objects.filter(date__year=year).filter(date__month=month).order_by('-date').reverse()
    return render(request, 'crawls/index.html',
                  {'crawls': crawls, 'month': month, 'year': year, 'calendar': result_html})


# def crawl_detail(request,crawl_id):
#     crawl = get_object_or_404(ScrapyItem,pk=crawl_id)
#     return render(request,'crawls/crawl_detail.html',{'crawl': crawl})

def crawl_list(request):
    today = datetime.datetime.today()
    month = today.month
    crawls = ScrapyItem.objects.filter(date__month=month).order_by('-date').reverse()

    return render(request, 'crawls/crawl_list.html', {'crawls': crawls, 'month': month})


def crawl(request, month, year):
    if month is None and year is None:
        today = datetime.datetime.today()
        year = today.year
        month = today.month

    response = HttpResponse(content_type='text/csv;charset=Shift-JIS')
    response['Content-Disposition'] = 'attachment; filename="{}_{}.csv"'.format(year, month)

    sio = io.StringIO()
    writer = csv.writer(sio)
    crawls = ScrapyItem.objects.filter(date__year=year).filter(date__month=month).order_by('-date').reverse()
    writer.writerow(['title', 'address', 'date', 'url', 'img_url'])
    for crawl in crawls:
        writer.writerow([crawl.title, crawl.address, crawl.date, crawl.url, crawl.img_url])
    response.write(sio.getvalue().encode('utf-16'))
    return response


def article(request, month, year):
    if month is None and year is None:
        today = datetime.datetime.today()
        year = today.year
        month = today.month

    response = HttpResponse(content_type='text/plain;charset=Shift-JIS')
    response['Content-Disposition'] = 'attachment; filename="{}_{}.txt"'.format(year, month)

    sio = io.StringIO()
    crawls = ScrapyItem.objects.filter(date__year=year).filter(date__month=month).order_by('-date').reverse()
    for crawl in crawls:
        sio.write('<h4>{}</h4>\n\
<img src="{}"/><ul>\n\
<li style="list-style-type: none;">\
\n<li>\n{}\n</li>\n<li>{}</li></ul>\
[btn]<a href="{}"" target="_blank" rel="noopener noreferrer">予約サイトへ</a>[/btn]\n\n'.format(crawl.title, crawl.img_url,
                                                                                          crawl.date, crawl.address,
                                                                                          crawl.url))
    response.write(sio.getvalue().encode('utf-16'))
    return response



def day(request, year, month, day):
    crawls = ScrapyItem.objects.filter(date__year=year).filter(date__month=month).filter(date__day=day).order_by('-date').reverse()
    return render(request, 'crawls/day_list.html', {'crawls': crawls, 'month': month, 'day': day})


def count(request, year, month, day):
    return HttpResponse("aaaa")

class MonthCalendar(MonthCalendarMixin, generic.TemplateView):
    """月間カレンダーを表示するビュー"""
    template_name = 'crawls/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['month'] = self.get_month_calendar()
        context['crawls'] = ScrapyItem.objects.order_by('-date').reverse()
        return context
