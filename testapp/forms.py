from django import forms
from .models import News, Pages, Comments
from django.forms import ModelForm, TextInput, Textarea, FileInput, ModelChoiceField
from django.contrib.auth.forms import UserCreationForm


class SearchForm(forms.Form):
    search = forms.CharField(max_length=256)


class AddNewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "head", "image", "disc", "pages_news"]
        pages_news = ModelChoiceField(queryset=Pages.objects.all())
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "head": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок'
            }),
            "image": FileInput(attrs={
                'class': 'form-control'
            }),
            "disc": Textarea(attrs={
                'placeholder': 'Введите описание',
                'class': 'form-control'
            }),
        }


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "head", "image", "disc", "pages_news"]
        pages_news = ModelChoiceField(queryset=Pages.objects.all())
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "head": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок'
            }),
            "image": FileInput(attrs={
                'class': 'form-control'
            }),
            "disc": Textarea(attrs={
                'placeholder': 'Введите описание',
                'class': 'form-control'
            }),
        }


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['user_name', 'user_news', 'user_comment']
        widgets = {
            'user_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваша юзерка'}),
            'user_comment': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш коммент'}),

        }
