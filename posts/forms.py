from django import forms
from .models import Post


def phone_number(value):
    # mobile = str(value)
    print(type(value))
    if value[0:4] != '+996' and len(value) != 10:
        raise forms.ValidationError('Mobile phone should start with +996 and len must be 10digits')


class PostForm(forms.Form):
    title = forms.CharField(max_length=100, validators=[phone_number])
    image = forms.ImageField()
    body = forms.CharField(widget=forms.Textarea)


class PostEditForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'image', 'body']


class CommentForm(forms.Form):
    body = forms.CharField()


class SearchForm(forms.Form):
    search = forms.CharField()
