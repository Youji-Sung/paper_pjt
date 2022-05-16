from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    # 그냥 만들어 놓았으니 수정하세요~
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    # path('<int:article_pk>/detail/comments', views.comments_create, name='comment_create'),
    # path('<int:article_pk>/detail/', views.detail, name='detail'),
]
