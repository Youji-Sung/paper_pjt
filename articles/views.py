from django.shortcuts import get_object_or_404, redirect, render
from .models import Article

# Create your views here.


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
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

