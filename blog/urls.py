from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<entry_id>[0-9]+)/$', views.entry, name='entry'),
    url(r'^(?P<entry_id>[0-9]+)/comment/$', views.post_comment, name='post_comment'),
    url(r'^(?P<entry_id>[0-9]+)/upvote/$', views.upvote, name='upvote'),
    url(r'^(?P<entry_id>[0-9]+)/downvote/$', views.downvote, name='downvote'),
    #url(r'^(?P<entry_id>[0-9]+)/(?P<comment_id>[0-9]+)/upvote/$', views.comm_upvote, name='comm_upvote'),
    #url(r'^(?P<entry_id>[0-9]+)/(?P<comment_id>[0-9]+)/downvote/$', views.comm_downvote, name='comm_downvote'),
]
