from django.contrib import admin
# 게시글(Post) Model을 불러옴
from .models import Post

# Register your models here.
# 관리자(admin)가 게시글(Post) 접근 가능
admin.site.register(Post)