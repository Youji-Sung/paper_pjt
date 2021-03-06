from .forms import CommentForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Article,Comment
from .forms import ArticleForm

# Create your views here.

# [김동신] 댓글 Create / template에 적용 완료
def comment_create(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid() :
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)


# [김동신] 댓글 Delete
def comment_delete(request, comment_pk, article_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if comment.password == request.POST.get("password") :
        comment.delete()
    return redirect('articles:detail', pk=article_pk)

# [김동신] 댓글 Update
def comment_update(request, article_pk, comment_pk):
    article = get_object_or_404(Article,pk=article_pk)
    comment = get_object_or_404(Comment,pk=comment_pk)
    # template에서 form 활용해서 비번 받아올 것
    if request.POST.get('password') == comment.password :
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save()
            return redirect('articles:detail', article_pk)
    
    else :
        comment_form = CommentForm(instance=comment)
    context = {
        'article' : article,
        'comment' : comment,
        'comment_form' : comment_form,
    }
    return render(request, 'articles/comment_update.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.like = 0
            article.save()
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
    


def likes(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.like += 1

    return redirect('articles:detail', pk)

# 댓글 목록 및 댓글 작성 추가
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()

    context = {
        'article': article,
        "comments" : comments,
        "comment_form" : comment_form,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        if request.POST.get('password') == article.password:    
            article.delete()
            return redirect('articles:index')
    context = {
        'article' : article
    }

    return render(request, 'articles/delete.html', context)

def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        if request.POST.get('password') == article.password:   
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        
    else:
        form = ArticleForm(instance=article)

    context = {
        'article': article,
        'form' : form,
    }
    return render(request,'articles/update.html', context)

