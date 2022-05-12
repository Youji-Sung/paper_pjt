from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
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
    
def detail(request,article_pk):
    pass


def likes(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.like += 1
    context = {
        'liked' : article.like,
    }
    return JsonResponse(context)

