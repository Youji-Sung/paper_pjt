from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # 그냥 만들어 놓았으니 수정하세요~
    path('<int:article_pk>/detail/comments', views.comments_create, name='comment_create'),
]
