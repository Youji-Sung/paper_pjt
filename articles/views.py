from .forms import CommentForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Article,Comment
from .forms import ArticleForm

# Create your views here.


# [김동신] 댓글 Read (나중에 index 작성되면 따로 합쳐야될 듯)
def comment(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    comments = article.comment_set.all()
    context = {
        "comments" : comments,
    }
    return render(request, 'articles/index.html', context)


# [김동신] 댓글 Create(나중에 detail page랑 합쳐야됨)
def comment_create(request):
    comment = CommentForm()
    context = {
        'comment' : comment
    }
    return render(request, 'articles/comment.html', context)

# [김동신] 댓글 Delete
def comment_delete(request, comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    comment.delete()
    return redirect('comment:create')

# [김동신] 댓글 Update
def comment_update(request, comment_pk):
    comment_form = CommentForm(request.POST)
    context = {
        'form':comment_form,
    }
    return render(request, 'articles/comment_update.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
    
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
    


def likes(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.like += 1
    context = {
        'liked' : article.like,
    }
    return JsonResponse(context)
    
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 비밀번호가 같다면! 추가해야 함
    article.delete()
    return redirect('articles.index')

def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 비밀번호가 같다면! 추가해야 함
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        'article': article,
        'form' : form,
    }
    return render(request,'article/update.html', context)

