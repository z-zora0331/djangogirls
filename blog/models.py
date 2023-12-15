from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
### Function name永遠要大寫，models.Model代表要存進資料庫
class Post(models.Model):
    ### models.ForeignKey - 與其他 model 的關聯。
    ### models.CharField - 定義一個有上限的字元。
    ### models.TextField - 定義一個有無上限的字串。
    ### models.DateTimeField - 日期與時間。

    author         = models.ForeignKey(User, on_delete=models.CASCADE)
    title          = models.CharField(max_length=200)
    text           = models.TextField()
    created_date   = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # Method
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post             = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author           = models.CharField(max_length=200)
    text             = models.TextField()
    created_date     = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def disapprove(self):
        self.approved_comment = False
        self.save()

    def __str__(self):
        return self.text