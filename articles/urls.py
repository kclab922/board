from django.urls import path
# 같은 폴더 내에 있는 views를 불러올게요
from . import views

app_name = 'articles'

urlpatterns = [
    # '': articles/ 에 해당하는 정보만 받겠다
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),

    # input 넣을 수 있는 빈 도화지 페이지 만들기
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
 