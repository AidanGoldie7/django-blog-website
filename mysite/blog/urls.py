from django.conf.urls import url
from blog import views 

urlpatterns = [
    #homepage url
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    #about page url
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    #blog post details url
    url(r'post/(?P<pk>\d+)$', views.PostDetailView.as_view(),name='post_detail'),
    #create new blog post url
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    #update/edit blog post url
     url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    #delete blog post url 
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    #blog post drafts url 
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),


]