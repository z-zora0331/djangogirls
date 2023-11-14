from django.urls import path, re_path
from . import views

urlpatterns = [
    # 首頁
    re_path(r'^$', views.post_list),
    # path('', views.post_list, name='post_list'),

    # 文章
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # 新增文章
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    # path('post/new/', views.post_new, name='post_new'),

    # 修改文章
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]