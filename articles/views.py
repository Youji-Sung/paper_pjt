from django.shortcuts import render, redirect, get_object_or_404

from articles.models import Article, Comment

from .forms import CommentForm

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



