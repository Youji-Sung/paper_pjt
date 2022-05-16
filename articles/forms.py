from django import forms
from .models import Comment, Article

# [김동신] 댓글 작성 form
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
