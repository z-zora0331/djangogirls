from django.urls import path, re_path
from . import views

urlpatterns = [
    # 首頁
    re_path(r'^$', views.post_list),
    # path('', views.post_list, name='post_list'),

    # 已發佈文章
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # 新增文章
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    # path('post/new/', views.post_new, name='post_new'),

    # 修改文章
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    # 草稿文章
    re_path(r'^drafts/$', views.post_draft_list, name='post_draft_list'),

    # 發佈文章
    re_path(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),

    # 刪除文章
    re_path(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),

    # 新增評論
    re_path(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),

    # 刪除評論
    re_path(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),

    # 核准評論
    re_path(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
]