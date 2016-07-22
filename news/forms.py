from django import forms
from .models import NewsItem,Comment


class NewsForm(forms.ModelForm):

    class Meta:

        model = NewsItem  # tells django which model should be used to create this form
        fields = ('news_title', 'text',)  # says which fields should end up in our form


class CommentForm(forms.ModelForm):

        class Meta:
            model = Comment
            fields = ('author', 'text',)

