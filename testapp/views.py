from django.shortcuts import render, redirect
from . import models, forms
from .models import News, Pages, Comments
from .forms import AddNewsForm, CommentsForm, NewsForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views import View


# Create your views here.
def home(request):
    # Поисковая строка
    search_bar = forms.SearchForm()
    # Все категории
    pages_all = Pages.objects.all()
    # Все про новости
    news_all = News.objects.all()
    # Отправка элементов на фронт
    context = {
        'pages': pages_all,
        'news': news_all
    }
    return render(request, 'home.html', context)


# Вывод таблицы категорий
def get_all_pages(request, pk):
    pages = Pages.objects.get(id=pk)
    news = News.objects.filter(pages_news=pages)
    # Отправка данных на фронт
    context = {
        'news': news,
    }
    return render(request, 'pages.html', context)


# Вывод информации о новостях
def get_all_news(request, pk):
    news = News.objects.get(id=pk)
    comment = Comments.objects.all()
    # Отправка данных на фронт
    context = {
        'news': news,
        'comment': comment
    }
    return render(request, 'news.html', context)


def add(request):
    error = ''
    if request.method == 'POST':
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            News.objects.create(title=form.cleaned_data.get('title'),
                                head=form.cleaned_data.get('head'),
                                image=form.cleaned_data.get('image'),
                                disc=form.cleaned_data.get('disc'),
                                pages_news=form.cleaned_data.get('pages_news'))
            return redirect('/')
    form = AddNewsForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'add.html', context)


# Поиск новости
def search_news(request):
    if request.method == 'POST':
        get_news = request.POST.get('search_news')
        try:
            exact_news = News.objects.get(title__icontains=get_news)
            return redirect(f'/news/{exact_news.id}')
        except:
            return redirect(f'/pg_not_found/')


# Если поиск не выдал результатов
def pg_not_found(request):
    return render(request, 'not_found.html')


# Регистрация
class Register(View):
    template_name = 'registration/register.html'

    # Отправка формы регистрации
    def get(self, request):
        context = {'form': UserCreationForm}
        return render(request, self.template_name, context)

        # Добавление в БД

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        context = {'form': UserCreationForm}
        return render(request, self.template_name, context)


def add_comment(request):
    error = ''
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            # Получаем выбранную новость из формы
            selected_news = form.cleaned_data['user_news']

            # Создаем объект комментария, связывая его с выбранной новостью
            comment = form.save(commit=False)
            comment.user_news = selected_news
            comment.save()
            # form.save()
            # return redirect('/')
        else:
            error = 'Недопустимый коммент('
    form = CommentsForm()
    context = {'form': form,
               'error': error}
    return render(request, 'add_comment.html', context)


def news_edit(request, news_id):
    error = ''
    news_instance = News.objects.get(id=news_id)

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news_instance)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
            error = 'Недопустимый текст'
    else:
        form = NewsForm(instance=news_instance)

    context = {'form': form, 'error': error}
    return render(request, 'edit.html', context)
