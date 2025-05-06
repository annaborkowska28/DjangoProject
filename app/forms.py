from django import forms
from app.models import Article

# class CreateArticle(forms.Form):
#     ARTICLE_STATUS = (
#     ("draft", "draft"),
#     ("inprogress", "in progress"),
#     ("published", "published")
#     )

#     title = forms.CharField(max_length=100)
#     status = forms.CharField(choices=ARTICLE_STATUS)
#     content = forms.CharField(widget=forms.Textarea)
#     word_count = forms.IntegerField()
#     twitter_post = forms.CharField(widget=forms.Textarea, required=False)

    #to use ModelForm
  

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'status', 'content', 'word_count', 'twitter_post')
