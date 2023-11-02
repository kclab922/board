from django.urls import path
# 같은 폴더 내에 있는 views를 불러올게요
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
]
 