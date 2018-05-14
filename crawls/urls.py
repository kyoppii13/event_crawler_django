from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'crawls'

urlpatterns = [
    #path('',views.top,name="top"),
    path('', views.MonthCalendar.as_view(), name='month'),
    path('<int:year>-<int:month>/',views.top,name="top"),
    path('month/<int:year>/<int:month>/', views.MonthCalendar.as_view(), name='month'),
    path('<int:year>/<int:month>/<int:day>', views.day, name='day'),
    path('count/<int:year>/<int:month>/<int:day>', views.count, name='count'),
    path('api/<int:year>/<int:month>/',views.crawl,name="out_csv"),
    path('article/<int:year>/<int:month>/',views.article,name="out_csv"),
    path('list/',views.crawl_list,name="crawl_list"),
               ]
