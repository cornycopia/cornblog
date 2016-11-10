from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<entry_id>[0-9]+)/$', views.entry, name='entry'),
    url(r'^(?P<entry_id>[0-9]+)/comment/$', views.post_comment, name='post_comment'),
    #url(r'^$', views.IndexView.upvote(), name='upvote'),
]
