from django.shortcuts import render
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