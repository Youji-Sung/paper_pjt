from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # 그냥 만들어 놓았으니 수정하세요~
    # [김동신] 댓글 관련 URL
    path('<int:pk>/', views.detail, name='detail'),
    path('comments/', views.comment_create, name='comment_create'),
    path('comments/<int:comment_pk>/delete', views.comment_delete, name='comment_delete'),
    path('comments/<int:comment_pk>/update', views.comment_update, name='comment_update'),
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    # path('<int:article_pk>/detail/comments', views.comments_create, name='comment_create'),
    # path('<int:article_pk>/detail/', views.detail, name='detail'),
]
