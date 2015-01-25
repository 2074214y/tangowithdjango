from django.conf.urls import patterns, url
from newproject import views

urlpatterns = patterns('',
                       url(r'^$',views.index, name='index'))