from django.urls import path
from . import views # bütün view ün dahil edilmesi

urlpatterns = [
    path('',views.post_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail,name='post_detail'),
    path('post/new',views.post_new,name='post_new'),
    path('post/<int:pk>/edit/',views.post_edit,name='post_edit'),
    path('drafts/',views.post_draft_list,name='post_draft_list'),
    path('post/<pk>/publish/',views.post_publish,name='post_publish'),
    path('post/<pk>/remove',views.post_remove,name='post_remove'),
    path('post/<int:pk>/comments/', views.add_comment,name='add_comment'),
    path('post/<int:pk>/remove/',views.remove_comment,name='remove_comment'),
    path('post/<int:pk>/approve/',views.approve_comment,name='approve_comment'),
]
