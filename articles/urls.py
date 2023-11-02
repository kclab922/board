from django.urls import path
# 같은 폴더 내에 있는 views를 불러올게요
from . import views

app_name = 'articles'

urlpatterns = [
    # '': articles/ 에 해당하는 정보만 받겠다
    path('', views.index, name='index'),
]
 