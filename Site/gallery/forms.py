from django import forms
from django_markdown.widgets import MarkdownWidget
from gallery.models import CommentForImage


class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=256, widget=MarkdownWidget(attrs={'maxlength': 256}))

    class Meta:
        model = CommentForImage
        fields = ['comment']


class DeleteCommentForm(forms.ModelForm):

    class Meta:
        model = CommentForImage
        fields = []
