from django.db import models

# Create your models here.

# Model이라는 클래스를 상속받아옴
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


