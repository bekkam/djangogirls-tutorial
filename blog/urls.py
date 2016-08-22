from django.conf.urls import url
from . import views

urlpatterns = [
    # assign a view called post_list to ^$ URL - matches empty string ('http://127.0.0.1:8000/'')
    # name='post_list' is the name of the URL that will be used to identify the view
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

]
