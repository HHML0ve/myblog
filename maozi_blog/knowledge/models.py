from django.db import models


# Create your models here.
class article(models.Model):
    article_title = models.CharField('article title', max_length=200)
    article_content = models.CharField('main content',  max_length=200)
    article_example = models.CharField(max_length=200)
    article_date = models.DateTimeField('last mark')
