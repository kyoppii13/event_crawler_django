from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('',views.top,name="top"),
    path('<int:year>-<int:month>/',views.top,name="top"),
    path('api/<int:year>-<int:month>/',views.crawl,name="out_csv"),
    path('article/<int:year>-<int:month>/',views.article,name="out_csv"),
    # path('add/',views.crawl_edit,name="crawl_add"),
    path('list/',views.crawl_list,name="crawl_list"),
    # path('<int:crawl_id>/', views.crawl_detail, name='crawl_detail'),
    # path('del/<int:crawl_id>/', views.crawl_del, name='crawl_del'),
    # path('mod/<int:crawl_id>/', views.crawl_edit, name='crawl_mod'),
               ]
