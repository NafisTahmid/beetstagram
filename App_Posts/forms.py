from django import forms
from App_Posts.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('image', 'caption')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'image', )