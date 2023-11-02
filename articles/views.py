from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# 전체 게시물을 가져오는 코드
def index(request):
    # Article이라는 클래스에서 객체 전체를 가져올게
    articles = Article.objects.all()

    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)


def detail(request, id):
    # 단일게시물이므로 article 단수형
    article = Article.objects.get(id=id)

    context = {
        'article': article,
    }
    
    return render(request, 'detail.html', context)


def new(request):
    return render(request, 'new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article()
    article.title = title
    article.contetn = content
    article.save()

    # 제출 후 인덱스로
    # return redirect('articles:index')

    # 제출 후 디테일로
    return redirect('articles:detail', id=article.id)