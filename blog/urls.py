from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)$', views.post_details, name='post_detail'),
    url(r'^category/(?P<category>\w+)$', views.category_posts, name='category_posts')
]
