from django import forms
from .models import Comment, Article

# [김동신] 댓글 작성 form
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content','nickname','password',)


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ('like',)
