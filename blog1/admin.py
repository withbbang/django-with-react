from django.contrib import admin
from .models import Post # admin 페이지에 Post table을 import 하겠다.

admin.site.register(Post)