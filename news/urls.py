from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.news_list, name='news_list'),
    #url(r'^accounts/profile/$', views.news_list, name='news_list'),
    url(r'^news/(?P<pk>\d+)/$', views.news_detail, name='news_detail'),
    url(r'^news/new/$', views.news_new, name='news_new'),
    url(r'^news/(?P<pk>\d+)/edit/$', views.news_edit, name='news_edit'),
    url(r'^news/(?P<pk>\d+)/comment/$', views.add_comment_to_news, name='add_comment_to_news'),

    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^drafts/$', views.news_draft_list, name='news_draft_list'),
    url(r'^news/(?P<pk>\d+)/publish/$', views.news_publish, name='news_publish'),
    url(r'^news/(?P<pk>\d+)/remove/$', views.news_remove, name='news_remove'),

]

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]