from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # 그냥 만들어 놓았으니 수정하세요~
    # [김동신] 댓글 관련 URL
    path('comments/', views.comment_create, name='comment_create'),
    path('comments/<int:comment_pk>/delete', views.comment_delete, name='comment_delete'),
    path('comments/<int:comment_pk>/update', views.comment_update, name='comment_delete'),
]
