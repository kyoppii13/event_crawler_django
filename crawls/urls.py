from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="top"),
    path('api/',views.crawl,name="out_csv"),
    # path('add/',views.crawl_edit,name="crawl_add"),
    path('list/',views.crawl_list,name="crawl_list"),
    # path('<int:crawl_id>/', views.crawl_detail, name='crawl_detail'),
    # path('del/<int:crawl_id>/', views.crawl_del, name='crawl_del'),
    # path('mod/<int:crawl_id>/', views.crawl_edit, name='crawl_mod'),
               ]
