from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add', views.add),
    path('search', views.search_news),
    path('pages/<int:pk>', views.get_all_pages),
    path('news/<int:pk>', views.get_all_news),
    path('pg_not_found/', views.pg_not_found),
    path('register', views.Register.as_view()),
    path('add-comments', views.add_comment),
    path('edit/<int:news_id>/', views.news_edit)
]


