from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^farmers-crop/$', views.farmers_grow_crop, name='crop'),
    url(r'^schedule/$', views.schedules_due_today_tom, name='schedule'),
    url(r'^bill/$', views.bill_for_fertiliser, name='bill'),
]