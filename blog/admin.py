from django.contrib import admin
from .models import Post

# Register your models here.
### 顯示於admin畫面
admin.site.register(Post)